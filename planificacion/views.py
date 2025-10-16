from django.shortcuts import render
from .models import Cliente, Vendedor, Proyecto


def index(request):
    lista_proyectos = Proyecto.objects.all()
    return render(request, "planificacion/index.html", context={"proyectos": lista_proyectos})

def planificacion(request):
    lista_proyectos = Proyecto.objects.all()
    return render(request, "planificacion/planificacion.html", context={"proyectos": lista_proyectos})