from django.views.generic import ListView, DetailView, CreateView
from .models import Moto, Marca
from .forms import MotoForm, MarcaForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

class MotoCreateView(CreateView):
    model = Moto
    form_class = MotoForm
    template_name = 'cadastrar_moto.html'
    success_url = reverse_lazy('motos:catalogo')

class MotoListView(ListView):
    model = Moto
    template_name = 'catalogo.html'

class CadastrarMarcaView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'cadastrar_marca.html'
    success_url = reverse_lazy('motos:cadastrar_moto')
