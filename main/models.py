from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=100, default='Honório Fraga')

    def __str__(self):
        return self.nome


class Serie(models.Model):
    serie = models.CharField(max_length=50, default='1M02')
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.serie


class Perfil(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, default=None, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, default=None, null=True)

    vendas = models.IntegerField(default=0)
    compras = models.IntegerField(default=0)
    livros_emprestados = models.IntegerField(default=0)
    livros_pegados = models.IntegerField(default=0)
    trocas = models.IntegerField(default=0)



    def __str__(self):
        return self.usuario.nome


class Categorias(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Livro(models.Model):
    img = models.ImageField(upload_to='capas_livros', null=True, default=True)
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(null=True, blank=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    vender = models.BooleanField(default=False)
    preco_venda = models.FloatField(default=0)

    emprestar = models.BooleanField(default=False)
    preco_emprestimo = models.FloatField(default=0)
    emprestado =  models.BooleanField(default=False)

    trocar = models.BooleanField(default=False  )

    def __str__(self):
        return self.nome

