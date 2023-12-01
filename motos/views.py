from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib import messages
from django.contrib.messages import views
from users.permissions import *
from django.db.models import F
    
class MotoCreateView(FuncionarioPermission, generic.CreateView):
    model = Moto
    form_class = MotoForm
    template_name = 'cadastrar_moto.html'
    success_url = reverse_lazy('motos:catalogo')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name="Funcionário").exists()

class MotoListView(generic.ListView):
    model = Moto
    template_name = 'catalogo.html'
    paginate_by = 16

    def get_queryset(self):
        queryset = super().get_queryset()
        modelo = self.request.GET.get('modelo')
        marca_id = self.request.GET.get('marca', None)
        preco = self.request.GET.get('preco')

        if modelo:
            queryset = queryset.filter(modelo__icontains=modelo)
        
        if marca_id:
            queryset = queryset.filter(marca_id=marca_id)

        if preco:
            queryset = queryset.filter(preco=preco)
            preco = self.convert_price(preco)

        order_by = self.request.GET.get('order_by', 'preco')  # Adicionado para obter o parâmetro de ordenação

        if order_by.startswith('-'):
            # Ordenação decrescente
            order_by_field = order_by[1:]
            queryset = queryset.order_by(F(order_by_field).desc())
        else:
            # Ordenação crescente
            queryset = queryset.order_by(F(order_by))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Marca.objects.all()
        context['marca_selecionada'] = self.request.GET.get('marca', None)
        return context
    
    def convert_price(self, price):
        return Decimal(price.replace('.', '').replace(',', '.'))

class Moto2ListView(FuncionarioPermission, generic.ListView):
    model = Moto
    template_name = "visualizar_motos.html"
    paginate_by = 6

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name="Funcionário").exists()

class MotoUpdateView(FuncionarioPermission, generic.UpdateView):
    model = Moto
    form_class = MotoForm
    success_url = reverse_lazy("motos:visualizar_motos")
    template_name = "cadastrar_moto.html"
   
    def form_valid(self, form):
        messages.success(self.request, "Cadastro Atualizado")
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name="Funcionário").exists()
    
class MotoDeleteView(FuncionarioPermission, views.SuccessMessageMixin,generic.DeleteView):
    model = Moto
    success_url = reverse_lazy("motos:visualizar_motos")

    def form_valid(self, form):
        messages.error(self.request, "Moto removida")
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name="Funcionário").exists()
    
class MotoDetailView(generic.DetailView):
    model = Moto
    template_name = "detalhar_motos.html"  

class CadastrarMarcaView(FuncionarioPermission, generic.CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'cadastrar_marca.html'
    success_url = reverse_lazy('motos:cadastrar_moto')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name="Funcionário").exists()
