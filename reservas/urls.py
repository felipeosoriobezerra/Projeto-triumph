from django.contrib import admin
from django.urls import path
from reservas.views import ReservaCreateView, ReservaDeleteView, ReservaDetailView, ReservasListView, ReservaUpdateView

app_name = "resevas"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cadastro_reserva/", ReservaCreateView.as_view(), name="cadastro_reserva"),
    path('visualizar_reservas/', ReservasListView.as_view(), name='visualizar_reservas'),
    path('remover_reserva/<int:pk>/', ReservaDeleteView.as_view(), name="remover_reserva"),
    path('detalhe_reserva/<int:pk>/', ReservaDetailView.as_view(), name='detalhe_reserva'),
    path('update/<int:pk>/', ReservaUpdateView.as_view(), name="editar"),
    ]