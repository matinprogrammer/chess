from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from django import forms


User = get_user_model()


class UserCreationForm(UserCreationForm):
    pass


class UserChangeForm(UserChangeForm):
    pass


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
