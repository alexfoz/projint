from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Ausencia(models.Model):
    descricao = models.TextField()
    dataDeInicio = models.DateField(max_length=10)
    dataDeFim = models.DateField(max_length=10)
    funcionarioId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
