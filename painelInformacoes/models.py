from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField


class PainelInformacoes(models.Model):

    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao: TextField = models.TextField()
    dataCriacao = models.CharField(max_length=12)

    def __str__(self):
        return self.descricao
