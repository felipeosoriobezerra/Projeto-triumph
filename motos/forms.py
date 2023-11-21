# forms.py
from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = '__all__'
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'imagem1':  ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem2':  ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem3':  ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem4':  ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem5':  ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MotoForm, self).__init__(*args, **kwargs)
        self.fields['ano'].widget.attrs.update({'class': 'form-control'})
        self.fields['preco'].widget.attrs.update({'class': 'form-control'})

