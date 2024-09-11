# app_imobiliaria/forms.py

from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['endereco', 'imovel', 'data_visita', 'horario_visita']
