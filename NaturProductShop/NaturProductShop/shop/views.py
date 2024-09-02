from django.shortcuts import render, redirect
from .models import Product
from cart.cart import Cart
from django.core.paginator import Paginator

def Products_home(request):
    cat = Product.cat_names
    productsList = {}
    for c in cat:
        catProdList = Product.objects.filter(productType=c, productStatus='В наличии')[:9]
        productsList[c] = catProdList

    cart = Cart(request)
    totalPrice = cart.get_total_price()
    context = {
        'productsList': productsList,
        'category': cat,
        'cart': cart,
        'totalPrice': totalPrice
    }
    return render(request, 'mainContent.html', context)

def ProductPageView(request, *args, **kwargs):
    prod_id = kwargs['pk']
    cat = Product.cat_names
    product = Product.objects.get(id=prod_id)
    cart = Cart(request)
    totalPrice = cart.get_total_price()
    context = {
        'product': product,
        'cart': cart,
        'category': cat,
        'totalPrice': totalPrice
    }
    return render(request, 'productPage.html', context)

def SearchView(request):
    cart = Cart(request)
    cat = Product.cat_names
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            result1 = Product.objects.annotate(uppered_name=Upper('name')).filter(productName__contains=query.lower())
            result2 = Product.objects.filter(productType__icontains=query)
            result3 = Product.objects.filter(productDescription__icontains=query)
            result = result1 | result2 | result3
            paginator = Paginator(result, 3)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)
            return render(request, 'search.html', { 'result': query, 'cart': cart, 'category': cat, "page_obj": page_obj})
    return redirect('home')


