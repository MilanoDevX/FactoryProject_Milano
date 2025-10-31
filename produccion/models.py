from django.db import models
from planificacion.models import Proyecto, Cliente


class Produccion(models.Model):
    numero_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="producciones_proyecto")
    horas_disenio_teo = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="producciones_disenio_teo", null=True, blank=True)
    horas_fabricacion_teo = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="producciones_fabricacion_teo", null=True, blank=True)
    horas_montaje_teo = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="producciones_montaje_teo", null=True, blank=True)
    horas_disenio_real = models.FloatField()
    horas_fabricacion_real = models.FloatField()
    horas_montaje_real = models.FloatField()
    incidencias = models.CharField(max_length=200, null=True, blank=True)

def __str__(self):
        return f"Producción de {self.proyecto.numero_proyecto}"