from django.db import models


class Feedback(models.Model):
    descricao = models.TextField()
    data = models.CharField(max_length=12)
    responsavel = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
# Create your models here.
