from django.shortcuts import render
from .models import Cliente, Vendedor, Proyecto


def index(request):
    return render(request, "planificacion/index.html")

def proyectos(request):
    lista_proyectos = Proyecto.objects.all()
    return render(request, "planificacion/proyectos.html", context={"proyectos": lista_proyectos})

def clientes(request):
    lista_clientes = Cliente.objects.all()
    return render(request, "planificacion/clientes.html", context={"clientes": lista_clientes})

def vendedores(request):
    lista_vendedores = Vendedor.objects.all()
    return render(request, "planificacion/vendedores.html", context={"vendedores": lista_vendedores})