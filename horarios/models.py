from django.db import models
from departamento.models import Departamento


# Create your models here.

class Horarios(models.Model):
    horario = models.TextField(max_length=20)
    entrada = models.TimeField()
    saida = models.TimeField()
    departamentoId = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    #def __str__(self):
        #return Horarios
