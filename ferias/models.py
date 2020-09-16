from django.db import models
from usuario.models import Usuario


class Ferias(models.Model):
    dataInicio = models.CharField(max_length=50)
    dataFim = models.CharField(max_length=50)
    descricao = models.TextField()
    justificativa = models.TextField()
    Usuario.solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Usuario.aprovador =  models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.solicitante
