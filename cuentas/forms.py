from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from cuentas.models import Perfil


class PerfilCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ("username", "email")


class PerfilChangeForm(UserChangeForm):
    class Meta:
        model = Perfil
        fields = ("avatar", "username", "first_name", "last_name", "pais", "direccion", "password")
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de usuario"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
            "pais": forms.TextInput(attrs={"class": "form-control", "placeholder": "País"}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Dirección"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "readonly": "readonly"}),
        }