from django.shortcuts import render, redirect
from . import views
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from shop.models import Order, OrderProduct, Product
from .models import User, Request
from .forms import CustomUserCreationForm, UserRequestForm, AnswerToRequestForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def UserRequestView(request, user):
    user_obj = User.objects.get(username=user)
    if request.method == 'GET':
        form = UserRequestForm()
        username = user_obj.username
        email = user_obj.email
        return render(request, 'request.html', {'form': form, 'username': username, 'email': email})

    if request.method == 'POST':
        form = UserRequestForm(request.POST)
        form.instance.userId = user_obj
        form.instance.userEmail = user_obj.email
        print(form.instance.userEmail)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'request.html', {'form': form})


def HistoryView(request, user):
    user_obj = User.objects.get(username=user)
    orders = Order.objects.filter(orderUser=user_obj)
    order_products = {}
    for order in orders:
        order_products[order] = {}
        for order_product in OrderProduct.objects.filter(OrderId=order):
            product = Product.objects.get(id=order_product.ProductId.id)
            order_products[order][order_product] = product
    print(order_products)
    return render(request, 'history.html', {'order_products': order_products})

def sign_up(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/signup.html', {'form': form})

def YourRequestsView(request, user):
    user_obj = User.objects.get(username=user)
    requests = Request.objects.filter(userId=user_obj)
    return render(request, 'yourRequests.html', {'requests': requests})

def UsersRequestsView(request):
    requests = Request.objects.filter(answerText='Ждите ответ менеджера')
    return render(request, 'userRequests.html', {'requests': requests})

def AnswerToRequestView(request, req):
    reqe = Request.objects.get(id=req)
    if request.method == 'GET':
        form = AnswerToRequestForm()
        return render(request, 'answerToRequest.html', {'form': form, 'request': reqe})

    if request.method == 'POST':
        form = AnswerToRequestForm(request.POST, instance=reqe)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'answerToRequest.html', {'form': form})
