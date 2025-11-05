from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash   
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
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


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = PerfilChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("cuentas:profile_detail")
    else:
        form = PerfilChangeForm(instance=request.user)
    return render(request, "cuentas/perfil_editar.html", {"form": form})


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("cuentas:profile_detail")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"¡Bienvenido {user.username}!")
                return redirect("/")
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Datos inválidos. Intenta nuevamente.")
    else:
        form = AuthenticationForm()
    return render(request, "cuentas/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, "cuentas/logout.html")


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)   # Mantener la sesión activa después del cambio de contraseña
            messages.success(request, "¡Tu contraseña ha sido actualizada correctamente!")
            return redirect("cuentas:profile_detail")
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "cuentas/cambiar_contrasena.html", {"form": form})