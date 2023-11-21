from django.views.generic import ListView, DetailView, CreateView
from .models import Moto, Marca
from .forms import MotoForm, MarcaForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib import messages
from django.contrib.messages import views

class MotoCreateView(generic.CreateView):
    model = Moto
    form_class = MotoForm
    template_name = 'cadastrar_moto.html'
    success_url = reverse_lazy('motos:catalogo')

class MotoListView(generic.ListView):
    model = Moto
    template_name = 'catalogo.html'

class Moto2ListView(generic.ListView):
    model = Moto
    template_name = "visualizar_motos.html"
    paginate_by = 4

class MotoUpdateView(generic.UpdateView):
    model = Moto
    form_class = MotoForm
    success_url = reverse_lazy("motos:visualizar_motos")
    template_name = "cadastrar_moto.html"
   
    def form_valid(self, form):
        messages.success(self.request, "Cadastro Atualizado!")
        return super().form_valid(form)
    
class MotoDeleteView(views.SuccessMessageMixin,generic.DeleteView):
    model = Moto
    success_url = reverse_lazy("motos:visualizar_motos")
    success_message = "Cadastro deletado!"

class CadastrarMarcaView(generic.CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'cadastrar_marca.html'
    success_url = reverse_lazy('motos:cadastrar_moto')
