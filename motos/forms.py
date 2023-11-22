from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput
from decimal import Decimal

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
            'imagem_1':  ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem_2':  ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem_3':  ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem_4':  ClearableFileInput(attrs={'class': 'form-control'}),
            'imagem_5':  ClearableFileInput(attrs={'class': 'form-control'}),
        }

        preco = forms.DecimalField(
    widget=forms.TextInput(attrs={
        'class': 'money form-control',
        'placeholder': 'Preço'
    }), localize=True
)

    def __init__(self, *args, **kwargs):
        super(MotoForm, self).__init__(*args, **kwargs)
        self.fields['ano'].widget.attrs.update({'class': 'form-control'})

    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        if ano < 1000 or ano > 9999:
            raise forms.ValidationError('O ano deve ter 4 dígitos.')
        return ano
    
