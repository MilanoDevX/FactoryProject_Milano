from django.shortcuts import render
from produccion.forms import ProduccionForm
from produccion.models import Produccion
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def produccion(request):
    return render(request, "produccion/produccion.html")


class ProduccionListView(LoginRequiredMixin, ListView):
    model = Produccion
    template_name = "produccion/produccion_list.html"
    context_object_name = "produccion_list"

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        queryset = Produccion.objects.all().order_by("-numero_proyecto")
        if query:
            queryset = queryset.filter(numero_proyecto__numero_proyecto__icontains=query)
        return queryset
    

class ProduccionCreateView(LoginRequiredMixin, CreateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = "produccion/produccion_form.html"
    success_url = reverse_lazy("produccion:produccion_list")


class ProduccionUpdateView(LoginRequiredMixin, UpdateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = "produccion/produccion_form.html"
    success_url = reverse_lazy("produccion:produccion_list")
    def get_object(self):
        numero = self.kwargs.get("numero_proyecto")
        return Produccion.objects.get(numero_proyecto__numero_proyecto=numero)


class ProduccionDeleteView(LoginRequiredMixin, DeleteView):
    model = Produccion
    template_name = "produccion/produccion_confirm_delete.html"
    success_url = reverse_lazy("produccion:produccion_list")

    def get_object(self):
        numero = self.kwargs.get("numero_proyecto")
        return Produccion.objects.get(numero_proyecto__numero_proyecto=numero)


class ProduccionDetailView(LoginRequiredMixin, DetailView):
    model = Produccion
    template_name = "produccion/produccion_detail.html"
    context_object_name = "produccion"

    def get_object(self):
        numero = self.kwargs.get("numero_proyecto")
        return Produccion.objects.get(numero_proyecto__numero_proyecto=numero)







