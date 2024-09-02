from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import CartConfirmOrder
from .cart import Cart
from shop.models import OrderProduct, Product
from users.models import User
from .forms import CartAddProductForm, CartConfirmOrder




def cart_add(request, product_id):
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product_id=product_id,
            quantity= 1,
            update_quantity=cd['update'])
    print(cart)
    return redirect('cart')

def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('home')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart, 'form': CartConfirmOrder})

def confirm_order(request, user):
    cart = Cart(request)
    user_obj = User.objects.get(username=user)
    if request.method == 'POST':
        form = CartConfirmOrder(request.POST)
        form.instance.orderUser = user_obj
        print(form.instance.orderUser)
        form.instance.orderCost = cart.get_total_price()
        print(form.instance.orderCost)
        print(form.as_div())
        if form.is_valid():
            order = form.save()
            for item in cart:
                product = Product.objects.get(pk=item['pk'])
                OrderProduct.objects.create(OrderId=order,
                                            ProductId=product,
                                            ProductAmount=item['quantity'])
            cart.clear()
            return redirect('home')
        else:
            return render(request, "cart.html", {"form": form, 'cart': cart})


