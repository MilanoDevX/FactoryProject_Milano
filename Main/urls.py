from django.urls import path
from Main import views

app_name = "Main"

urlpatterns = [
    path ("", views.index, name="index"),
    

]