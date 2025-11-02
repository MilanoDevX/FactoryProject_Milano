from django.urls import path
from planificacion import views

app_name = "planificacion"

urlpatterns = [
    path ("planificacion/", views.planificacion, name="planificacion"),
    path ("clientes/", views.clientes, name="clientes"),
    path ("clientes/crear", views.crear_cliente, name="crear_cliente"),
    path ("vendedores/", views.vendedores, name="vendedores"),
    path ("vendedores/crear", views.crear_vendedor, name="crear_vendedor"),
    path ("proyectos/", views.proyectos, name="proyectos"),
    path ("proyectos/crear", views.crear_proyecto, name="crear_proyecto"),
    path("proyectos/<int:numero_proyecto>/", views.detalles_proyecto, name="detalles_proyecto"),
    path("proyectos/<int:numero_proyecto>/editar/", views.editar_proyecto, name="editar_proyecto"),
    path("proyectos/<int:numero_proyecto>/eliminar/", views.eliminar_proyecto, name="eliminar_proyecto"),


]