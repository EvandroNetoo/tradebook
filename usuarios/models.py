from django.db import models
from main.models import *

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self):
       return self.nome
    

    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)
        Perfil(usuario=self).save()