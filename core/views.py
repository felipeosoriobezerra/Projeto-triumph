from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(generic.TemplateView):
    template_name = "index.html"
    
class ContactView(generic.TemplateView):
    template_name = "contato.html"
