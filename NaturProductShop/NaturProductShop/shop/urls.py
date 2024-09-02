from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductPageView, name='productPage'),
    path('search/', views.SearchView, name='search'),
]

