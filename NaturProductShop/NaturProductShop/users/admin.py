from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from shop.models import Product, Order, OrderProduct
from .models import User, Employee, Request
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email']
    model = Employee

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'orderDate', 'orderAddress', 'orderPhoneNumber', 'orderStatus')
    search_fields = ('id', 'orderAddress', 'orderPhoneNumber', 'orderStatus')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'productName', 'productType', 'productCost')
    search_fields = ('id', 'productName', 'productType', 'productDescription')

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'OrderId', 'ProductId', 'ProductAmount')
    search_fields = ('id', 'OrderId', 'ProductId', 'ProductAmount')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'employeeJobTitle')
    search_fields = ('id', 'user', 'employeeJobTitle')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'userEmail', 'requestText')
    search_fields = ('id', 'userId', 'userEmail', 'requestText')

admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)

admin.site.site_title = 'Админ-панель сайта "НатурПродукт"'
admin.site.site_header = 'Админ-панель сайта "НатурПродукт"'
