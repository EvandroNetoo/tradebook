from django.contrib import admin
from .models import *


'''list_display = ("id", "usuario", "legenda", "publicada")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10'''

class ListandoPerfil(admin.ModelAdmin):
    list_display = ("id", "usuario")
    list_display_links = ("id","usuario")
    search_fields = ("usuario",)
    list_per_page = 10

admin.site.register(Perfil, ListandoPerfil)


class ListandoLivro(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 10


admin.site.register(Livro, ListandoLivro)


class ListandoCategorias(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("nome",)
    list_per_page = 10


admin.site.register(Categorias, ListandoCategorias)


class ListandoEscola(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("nome",)
    list_per_page = 10


admin.site.register(Escola, ListandoEscola)


class ListandoSerie(admin.ModelAdmin):
    list_display = ("id", "serie")
    list_display_links = ("id","serie")
    search_fields = ("serie",)
    list_filter = ("serie",)
    list_per_page = 10


admin.site.register(Serie, ListandoSerie)