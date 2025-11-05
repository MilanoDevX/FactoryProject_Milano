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
        fields = ("avatar", "username", "first_name", "last_name", "pais", "direccion")
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control", 
                                               "placeholder": "Nombre de usuario", 
                                               "readonly": "readonly",}),   # para mostrar este campo visualmente bloqueado
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
            "pais": forms.TextInput(attrs={"class": "form-control", "placeholder": "País"}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Dirección"}),
        }

    # Para eliminar completamente el campo de contraseña del formulario de editar perfil
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "password" in self.fields:
            del self.fields["password"]

