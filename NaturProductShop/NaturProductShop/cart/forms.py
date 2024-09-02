import datetime
from django.utils import timezone

from django import forms
from shop.models import Order
from .cart import Cart
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, required=False,  coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CartConfirmOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderAddress', 'orderDate', 'orderPhoneNumber', 'orderPayment']
        widgets = {
            'orderDate': DateTimePickerInput()
        }


