from django.db import models


class Ferias(models.Model):
    dataInicio = models.CharField(max_length=50)
    dataFim = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.descricao
