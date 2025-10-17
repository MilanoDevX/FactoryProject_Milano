from django.shortcuts import render, redirect
from .models import Cliente, Vendedor, Proyecto
from .forms import *


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


def crear_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proyectos")
    else:
        form = ProyectoForm()
    return render(request, "planificacion/crear_proyecto.html", context={"form": form})


def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes")
    else:
        form = ClienteForm()
    return render(request, "planificacion/crear_cliente.html", context={"form": form})


def crear_vendedor(request):
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vendedores")
    else:
        form = VendedorForm()
    return render(request, "planificacion/crear_vendedor.html", context={"form": form})