from django.shortcuts import render
from produccion.forms import ProduccionForm
from produccion.models import Produccion
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.http import JsonResponse
from planificacion.models import Proyecto



def produccion(request):
    return render(request, "produccion/produccion.html")


class ProduccionListView(ListView):
    model = Produccion
    template_name = "produccion/produccion_list.html"
    context_object_name = "produccion_list"

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Produccion.objects.filter(numero_proyecto=query). order_by("-numero_proyecto")
        return Produccion.objects.all()
    

class ProduccionCreateView(CreateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = "produccion/produccion_form.html"
    success_url = reverse_lazy("produccion:produccion_list")


class ProduccionUpdateView(UpdateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = "produccion/produccion_form.html"
    success_url = reverse_lazy("produccion:produccion_list")
    def get_object(self):
        # Obtiene el número de proyecto desde la URL
        numero = self.kwargs.get("numero_proyecto")
        # Busca la producción cuyo número de proyecto coincida
        return Produccion.objects.get(numero_proyecto__numero_proyecto=numero)


class ProduccionDeleteView(DeleteView):
    model = Produccion
    template_name = "produccion/produccion_confirm_delete.html"
    success_url = reverse_lazy("produccion:produccion_list")

    def get_object(self):
        # Obtiene el número de proyecto desde la URL
        numero = self.kwargs.get("numero_proyecto")
        # Busca la producción cuyo número de proyecto coincida
        return Produccion.objects.get(numero_proyecto__numero_proyecto=numero)


class ProduccionDetailView(DetailView):
    model = Produccion
    template_name = "produccion/produccion_detail.html"
    context_object_name = "produccion"

    def get_object(self):
        # Obtiene el número de proyecto desde la URL
        numero = self.kwargs.get("numero_proyecto")
        # Busca la producción cuyo número de proyecto coincida
        return Produccion.objects.get(numero_proyecto__numero_proyecto=numero)







