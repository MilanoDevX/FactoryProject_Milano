from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from cuentas.forms import PerfilCreationForm, PerfilChangeForm


def register(request):
    if request.method == "POST":
        form = PerfilCreationForm(request.POST) # incluir request.FILES si hay campo obligatorio de imagenes en el form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("cuentas:profile_detail")
    else:
        form = PerfilCreationForm()
    return render(request, "cuentas/registro.html", {"form": form})


@login_required
def profile_detail(request):
    return render(request, "cuentas/perfil_detalle.html", {"user": request.user})


def profile_edit(request):
    if request.method == "POST":
        form = PerfilChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("cuentas:profile_detail")
    else:
        form = PerfilChangeForm(instance=request.user)
    return render(request, "cuentas/perfil_editar.html", {"form": form})

