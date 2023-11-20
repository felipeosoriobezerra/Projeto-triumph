from django.forms import ModelForm
from django import forms
from decimal import Decimal
from .models import Stand

class StandForm(ModelForm):
    class Meta:
        model = Stand
        fields = '__all__'

    localizacao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    valor = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'money form-control', 'placeholder': 'Valor do stand'}), localize=True)

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        if isinstance(valor, str):
            try:
                valor = Decimal(valor.replace(",", ""))
            except ValueError:
                raise forms.ValidationError("Informe um número válido para o valor.")
        return valor
