from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente, Vendedor, Proyecto
from .forms import *


def planificacion(request):
    return render(request, "planificacion/planificacion.html")

def proyectos(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        lista_proyectos = Proyecto.objects.filter(
            cliente__nombre__icontains=busqueda).order_by("fecha_entrega")
    else:
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
            return redirect("planificacion:proyectos")
    else:
        form = ProyectoForm()
    return render(request, "planificacion/crear_proyecto.html", context={"form": form})


def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("planificacion:clientes")
    else:
        form = ClienteForm()
    return render(request, "planificacion/crear_cliente.html", context={"form": form})


def crear_vendedor(request):
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("planificacion:vendedores")
    else:
        form = VendedorForm()
    return render(request, "planificacion/crear_vendedor.html", context={"form": form})


def detalles_proyecto(request, numero_proyecto):
    proyecto = get_object_or_404(Proyecto, numero_proyecto=numero_proyecto)
    return render(request, "planificacion/proyectos_detail.html", {"proyecto": proyecto})


def editar_proyecto(request, numero_proyecto):
    proyecto = get_object_or_404(Proyecto, numero_proyecto=numero_proyecto)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, "El proyecto se ha actualizado correctamente.")
            return redirect("planificacion:proyectos")
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, "planificacion/proyectos_edit.html", {"form": form, "proyecto": proyecto})


def eliminar_proyecto(request, numero_proyecto):
    proyecto = get_object_or_404(Proyecto, numero_proyecto=numero_proyecto)
    if request.method == "POST":
        proyecto.delete()
        messages.success(request, "El proyecto se ha eliminado correctamente.")
        return redirect("planificacion:proyectos")
    return render(request, "planificacion/proyectos_confirm_delete.html", {"proyecto": proyecto})