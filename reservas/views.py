from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import GerentePermission


#lista#

class ReservasListView(LoginRequiredMixin, generic.ListView):
    model = Reserva
    template_name = "visualizar_reservas.html"
    paginate_by = 4

#CRUD#

class ReservaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:visualizar_reservas")
    template_name = "cadastro_reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Reserva cadastrada!")
        return super().form_valid(form)

class ReservaUpdateView(GerentePermission,LoginRequiredMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:visualizar_reservas")
    template_name = "cadastro_reserva.html"
   
    def form_valid(self, form):
        messages.success(self.request, "Reserva Atualizado!")
        return super().form_valid(form)

class ReservaDeleteView(GerentePermission,LoginRequiredMixin, views.SuccessMessageMixin,generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas:visualizar_reservas")
    success_message = "reserva deletada!"
  
#Detalhe#

class ReservaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reserva
    template_name = "detalhe_reserva.html"  