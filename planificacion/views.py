from django.shortcuts import render
from .models import Cliente, Vendedor, Proyecto


def index(request):
    lista_proyectos = Proyecto.objects.all()
    return render(request, "planificacion/index.html", context={"proyectos": lista_proyectos})

def proyectos(request):
    lista_proyectos = Proyecto.objects.all()
    return render(request, "planificacion/proyectos.html", context={"proyectos": lista_proyectos})