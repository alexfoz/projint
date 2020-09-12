from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Usuariot(object):
    pass


class Usuariot(models.Model):
    ticketId = models.ForeignKey(User, on_delete=models.CASCADE)
    Usuariot.suarioSolicitanteTicketId = models.ForeignKey(User, on_delete=models.CASCADE)
    dataUltimaAlteracao = models.DateField(max_length=10)
    Usuariot.SolicitadoId = models.ForeignKey(User, on_delete=models.CASCADE)
