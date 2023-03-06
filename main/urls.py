from django.urls import path
from . import views


urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),
    path('buscar/', views.buscar, name='buscar'),
    path('proposta/<int:id_livro>', views.proposta, name='proposta'),


    path('perfil/', views.perfil, name='perfil'),
    path('seus_livros_todos/', views.seus_livros_todos, name='seus_livros_todos'),
    path('seus_livros_emprestados/', views.seus_livros_emprestados, name='seus_livros_emprestados'),
    path('seus_livros_anunciados/', views.seus_livros_anunciados, name='seus_livros_anunciados'),

    path('detalhes_livro/<int:id_livro>', views.detalhes_livro, name='detalhes_livro'),

    path('adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
    path('atualizar_livro/<int:id_livro>', views.atualizar_livro, name='atualizar_livro'),
    path('excluir_livro/<int:id_livro>', views.excluir_livro, name='excluir_livro'),

    path('comprar_livro/<int:id_livro>', views.comprar_livro, name='comprar_livro'),
    path('pegar_emprestado_livro/<int:id_livro>', views.pegar_emprestado_livro, name='pegar_emprestado_livro'),
    path('trocar_livro/<int:id_livro>', views.trocar_livro, name='trocar_livro'),



]
