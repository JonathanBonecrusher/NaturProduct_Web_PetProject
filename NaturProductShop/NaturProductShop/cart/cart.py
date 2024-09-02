from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):

    # Инициализация корзины
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем пустую корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    # Добавить продукт в корзину или обновить его количество.
    def add(self, product_id, quantity = 1, update_quantity = False):
        product = Product.objects.get(pk=product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'pk': int(product_id),
                                     'price': int(product.productCost),
                                     'name': str(product.productName),
                                     'img': str(product.productImg.url),
                                     }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()


    # Удаление товара из корзины.
    def remove(self, product_id):
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] == 1:
                del self.cart[product_id]
            else:
                self.cart[product_id]['quantity'] -= 1
            self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True
        # Передача корзины из сессии в JS для отображения самой корзины на странице

    # Перебор элементов в корзине и получение продуктов из базы данных.
    def __iter__(self):
        for item in self.cart.values():
            item['price'] = int(item['price'])
            yield item

    # Подсчет всех товаров в корзине.
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # Подсчет стоимости товаров в корзине.
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())
    # Удаление корзины из сессии
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        return []

