from django.contrib import admin

from .models import *


@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ["numero_proyecto", "horas_disenio_teo", "horas_fabricacion_teo", "horas_montaje_teo", "horas_disenio_real", "horas_fabricacion_real", "horas_montaje_real"]
    list_filter = ["numero_proyecto", "horas_disenio_teo", "horas_fabricacion_teo", "horas_montaje_teo", "horas_disenio_real", "horas_fabricacion_real", "horas_montaje_real"]
    ordering = ["-numero_proyecto"]

