from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'motos'

urlpatterns = [
    path('catalogo/', MotoListView.as_view(), name='catalogo'),
    path('cadastrar/', MotoCreateView.as_view(), name='cadastrar_moto'),
    path('cadastrar/marca/', CadastrarMarcaView.as_view(), name='cadastrar_marca'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
