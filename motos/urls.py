from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'motos'

urlpatterns = [
    path('catalogo/', MotoListView.as_view(), name='catalogo'),
    path('cadastrar/', MotoCreateView.as_view(), name='cadastrar_moto'),
    path('cadastrar/marca/', CadastrarMarcaView.as_view(), name='cadastrar_marca'),
    path('visualizar_motos/', Moto2ListView.as_view(), name='visualizar_motos'),
    path('update/<int:pk>/', MotoUpdateView.as_view(), name="editar"),
    path('remover_motos/<int:pk>/', MotoDeleteView.as_view(), name="remover_motos"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
