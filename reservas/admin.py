from django.contrib import admin
from .models import Reserva


@admin.register(Reserva)
class StandAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa','categoria_empresa','cnpj','quitado',)
