from django.contrib import admin
from django.urls import path
from . import views
app_name = "core"

urlpatterns = [
    
    path("", views.HomeView.as_view(), name="index" ),
    path("contato/", views.ContactView.as_view(), name="contato" ),
    ]