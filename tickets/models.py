from django.contrib.auth.models import User
from django.db import models


class Tickets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assunto = models.TextField(max_length=140)
    descricao = models.TextField()
    dataCriacao = models.DateTimeField
    dataFim = models.DateField
    status = models.CharField(max_length=12)

    #def __str__(self):
        #return self.descricao
