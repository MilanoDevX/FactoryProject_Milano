from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from cuentas.views import *

app_name = "cuentas"

urlpatterns = [
    # path("login/", LoginView.as_view(template_name="cuentas/login.html", redirect_authenticated_user=True, next_page="cuentas:profile_detail"), name="login"),
    # path("logout/", LogoutView.as_view(template_name="cuentas/logout.html"), name="logout"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile_detail, name="profile_detail"),
    path("profile/edit/", profile_edit, name="profile_edit"),
    path("profile/cambiar-contrasena/", change_password, name="change_password"),


]