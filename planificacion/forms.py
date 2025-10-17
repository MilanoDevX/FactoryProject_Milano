from django import forms
from .models import Proyecto, Cliente, Vendedor

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["numero_proyecto", "fecha_inicio", "fecha_entrega", "cliente", "vendedor"]
        widgets = {
            "numero_proyecto": forms.NumberInput(attrs={'class': 'form-control'}),
            "fecha_inicio": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "fecha_entrega": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "cliente": forms.Select(attrs={'class': 'form-control'}),
            "vendedor": forms.Select(attrs={'class': 'form-control'}),
        }


