from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from reservas.models import Reserva
from stands.models import Stand

class HomeView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        return context
    
class ContactView(generic.TemplateView):
    template_name = "contato.html"
