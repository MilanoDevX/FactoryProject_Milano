from django.contrib import admin

from .models import *

#admin.site.register(Proyecto)   Visualización básica

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ["numero_proyecto", "fecha_inicio", "fecha_entrega", "fecha_ingreso", "cliente", "vendedor", "horas_disenio_teo", "horas_fabricacion_teo", "horas_montaje_teo",]
    list_filter = ["numero_proyecto", "fecha_inicio", "fecha_entrega", "fecha_ingreso", "cliente", "vendedor", "horas_disenio_teo", "horas_fabricacion_teo", "horas_montaje_teo",]
    raw_id_fields = ["cliente", "vendedor"]
    ordering = ["-numero_proyecto"]


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "direccion", "telefono", "email"]
    list_filter = ["nombre", "apellido"]
    ordering = ["nombre"]


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "telefono", "email"]
    list_filter = ["nombre", "apellido"]
    ordering = ["nombre"]
