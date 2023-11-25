from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput
from decimal import Decimal
from django.utils.translation import gettext_lazy as _

class CustomFileInput(forms.ClearableFileInput):
    clear_checkbox_label = ''

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MotoForm(forms.ModelForm):
     preco = forms.DecimalField(widget=forms.TextInput(attrs={"class": "money form-control"}))
     ano = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

     class Meta:
        model = Moto
        fields = '__all__'
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'imagem_1':  CustomFileInput(attrs={'class': 'form-control'}),
            'imagem_2':  CustomFileInput(attrs={'class': 'form-control'}),
            'imagem_3':  CustomFileInput(attrs={'class': 'form-control'}),
            'imagem_4':  CustomFileInput(attrs={'class': 'form-control'}),
            'imagem_5':  CustomFileInput(attrs={'class': 'form-control'}),
        }

     def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        if ano < 1960 or ano > 2025:
            raise forms.ValidationError('O ano deve ser válido, entre 1960 e 2025.')
        return ano 
    