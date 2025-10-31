from django import forms
from produccion.models import Produccion


class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ["numero_proyecto", "horas_disenio_real", "horas_fabricacion_real", "horas_montaje_real", "incidencias"]
        widgets = {
            "numero_proyecto": forms.Select(attrs={'class': 'form-control'}),
            "horas_disenio_real": forms.NumberInput(attrs={'class': 'form-control'}),
            "horas_fabricacion_real": forms.NumberInput(attrs={'class': 'form-control'}),
            "horas_montaje_real": forms.NumberInput(attrs={'class': 'form-control'}),
            "incidencias": forms.TextInput(attrs={'class': 'form-control'}),
        }

