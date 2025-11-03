from django.urls import path
from produccion.views import *


app_name = "produccion"

urlpatterns = [
    path ("", produccion, name="produccion"),
    path("list", ProduccionListView.as_view(), name="produccion_list"), 
    path("nuevo/", ProduccionCreateView.as_view(), name="produccion_create"),
    path("<int:numero_proyecto>/", ProduccionDetailView.as_view(), name="produccion_detail"),
    path("<int:numero_proyecto>/editar/", ProduccionUpdateView.as_view(), name="produccion_edit"),
    path("<int:numero_proyecto>/eliminar/", ProduccionDeleteView.as_view(), name="produccion_delete"),
]


