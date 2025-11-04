from django.contrib import admin

from .models import *


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "is_staff", "is_superuser", "pais", "fecha_de_nacimiento", "direccion"]
    list_filter = ["username", "email", "is_staff", "is_superuser", "pais",]
    ordering = ["username"]

