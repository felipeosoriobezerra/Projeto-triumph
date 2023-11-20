from django.forms import ModelForm
from django import forms
from .models import Reserva

class ReservaForm(ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'stand': forms.Select(attrs={'class': 'form-control' }),
        }