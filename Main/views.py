from django.shortcuts import render

def index(request):
    return render(request, "Main/index.html")

