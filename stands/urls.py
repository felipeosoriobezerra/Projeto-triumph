
from django.contrib import admin
from django.urls import path
from stands.views import StandCreateView, StandDeleteView, StandListView, StandUpdateView  

app_name = "stands"

urlpatterns = [
    path('stands_visualizar/', StandListView.as_view(), name='stands_visualizar'),
    path('stands_cadastro/', StandCreateView.as_view(), name="stands_cadastro"),
    path('remover_stand/<int:pk>/', StandDeleteView.as_view(), name="remover_stand"),
    path('update_stand/<int:pk>/', StandUpdateView.as_view(), name="editar_stand"),

]

