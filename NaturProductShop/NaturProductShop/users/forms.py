from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Request

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',  'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['requestText']

class AnswerToRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['answerText']
