from django.urls import path
from planificacion import views

app_name = "planificacion"

urlpatterns = [
    # path ("", views.index, name="index"),
    path ("planificacion/", views.planificacion, name="planificacion"),
    path ("proyectos/", views.proyectos, name="proyectos"),
    path ("clientes/", views.clientes, name="clientes"),
    path ("vendedores/", views.vendedores, name="vendedores"),
    path ("proyectos/crear", views.crear_proyecto, name="crear_proyecto"),
    path ("clientes/crear", views.crear_cliente, name="crear_cliente"),
    path ("vendedores/crear", views.crear_vendedor, name="crear_vendedor"),


]