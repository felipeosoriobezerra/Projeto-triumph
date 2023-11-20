from django.contrib import admin
from .models import Stand 

@admin.register(Stand)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('localizacao','valor',)