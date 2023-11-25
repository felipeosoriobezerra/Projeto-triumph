from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib import messages
from django.contrib.messages import views

class MotoCreateView(generic.CreateView):
    model = Moto
    form_class = MotoForm
    template_name = 'cadastrar_moto.html'
    success_url = reverse_lazy('motos:catalogo')

    def form_invalid(self, form):
        print (form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class MotoListView(generic.ListView):
    model = Moto
    template_name = 'catalogo.html'
    paginate_by = 16

class Moto2ListView(generic.ListView):
    model = Moto
    template_name = "visualizar_motos.html"
    paginate_by = 6

class MotoUpdateView(generic.UpdateView):
    model = Moto
    form_class = MotoForm
    success_url = reverse_lazy("motos:visualizar_motos")
    template_name = "cadastrar_moto.html"
   
    def form_valid(self, form):
        messages.success(self.request, "Cadastro Atualizado")
        return super().form_valid(form)
    
class MotoDeleteView(views.SuccessMessageMixin,generic.DeleteView):
    model = Moto
    success_url = reverse_lazy("motos:visualizar_motos")

    def form_valid(self, form):
        messages.error(self.request, "Cadastro cancelado")
        return super().form_valid(form)
    
class MotoDetailView(generic.DetailView):
    model = Moto
    template_name = "detalhar_motos.html"  

class CadastrarMarcaView(generic.CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'cadastrar_marca.html'
    success_url = reverse_lazy('motos:cadastrar_moto')
