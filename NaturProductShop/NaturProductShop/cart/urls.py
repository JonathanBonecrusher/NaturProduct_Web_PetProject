from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('clear/', views.cart_clear, name='clear'),
    path('add/<product_id>/', views.cart_add, name='cart_add'),
    path('remove/<product_id>/', views.cart_remove, name='cart_remove'),
    path('create/<user>/', views.confirm_order, name='order_create')
]

