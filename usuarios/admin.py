from django.contrib import admin
from .models import *


class ListandoUsuario(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id","nome")
    # readonly_fields = ('nome', 'email', 'senha')
    search_fields = ("nome",)
    list_per_page = 10
    
admin.site.register(Usuario, ListandoUsuario)
