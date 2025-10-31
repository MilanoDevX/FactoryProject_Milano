from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Proyecto(models.Model):
    numero_proyecto = models.IntegerField(unique=True)
    fecha_inicio = models.DateField()
    fecha_entrega = models.DateField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    horas_disenio_teo = models.FloatField(null=True)
    horas_fabricacion_teo = models.FloatField(null=True)
    horas_montaje_teo = models.FloatField(null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="proyectos")
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True, blank=True, related_name="proyectos")

    def __str__(self):
        return f"Proyecto: {self.numero_proyecto} - Cliente: {self.cliente.nombre} {self.cliente.apellido}"
     



    