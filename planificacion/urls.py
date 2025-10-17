from django.urls import path
from planificacion import views

urlpatterns = [
    path ("", views.index, name="index"),
    path ("proyectos/", views.proyectos, name="proyectos"),
    path ("clientes/", views.clientes, name="clientes"),
    path ("vendedores/", views.vendedores, name="vendedores"),

]