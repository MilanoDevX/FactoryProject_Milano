from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Bienvenidos a Planificación"}
    return render(request, "planificacion/index.html", context)