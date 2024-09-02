from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from users.models import User, Employee
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField



class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("Овощи", "Овощи"),
        ("Фрукты", "Фрукты"),
        ("Готовая продукция", "Готовая продукция"),
        ("Прочее", "Прочее"),
    ]

    PRODUCT_STATUS_CHOICES = [
        ("В наличии", "В наличии"),
        ("Не в начличии", "Не в начличии"),
    ]

    productName = models.TextField(max_length=50, verbose_name='Нименование')
    productType = models.TextField(choices=PRODUCT_TYPE_CHOICES, verbose_name='Тип продукта')
    productCost = models.DecimalField(max_digits=999, decimal_places=2, verbose_name='Стоимость')
    productStatus = models.TextField(choices=PRODUCT_STATUS_CHOICES, default='В наличии', verbose_name='Статус')
    productDescription = models.TextField(verbose_name='Описание')
    productImg = models.FileField(upload_to='static/img/prodImg', verbose_name='Изображение')

    cat_names = ["Овощи", "Фрукты", "Готовая продукция", "Прочее"]

    def __str__(self):
        return self.productName[:20]

    def get_absolute_url(self):
        return reverse('productPage', args=[str(self.id)])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Order(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ("КП", "Картой при получении"),
        ("НП", "Наличными при получении"),
    ]
    STATUS_CHOICES = [
        ("ОФ", "Оформлен"),
        ("СЗ", "Сбор заказа"),
        ("ДС", "Доставка курьером"),
        ("ДО", "Доставлен"),
    ]

    orderDate = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    orderAddress = models.CharField(max_length=50, verbose_name='Адрес доставки')
    orderCost = models.DecimalField(max_digits=999, decimal_places=2, verbose_name='Общая стоимость')
    orderPhoneNumber = PhoneNumberField(region="RU", verbose_name='Номер телефона', null=False)
    orderPayment = models.TextField(choices=PAYMENT_TYPE_CHOICES, verbose_name='Способ оплаты')
    orderStatus = models.TextField(choices=STATUS_CHOICES, default="Оформлен", verbose_name='Статус заказа')
    orderUser = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='Заказчик')

    def __str__(self):
        return f'Заказ №{self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['orderDate']


class OrderProduct(models.Model):
    OrderId = models.ForeignKey(Order, on_delete=models.CASCADE, default=1, verbose_name='Заказ')
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE, default=1, verbose_name='Продукт')
    ProductAmount = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Продукт в заказе'
        verbose_name_plural = 'Продукты в заказе'


