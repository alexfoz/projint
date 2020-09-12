from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from tickets.models import Tickets


class Usuariot(object):
    pass


class Usuariot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticketId = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    Usuariot.solicitante = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    dataUltimaAlteracao = models.DateField(max_length=10)
    Usuariot.solicitadoId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticketId