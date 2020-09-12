from django.db import models


# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=8)
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=20)
    telefone = models.CharField(max_length=14)
    dataDeNascimento = models.DateField(max_length=10)
    dataDeAdmissao = models.DateField(max_length=10)
    dataDeTermino = models.DateField(max_length=10)
    matricula = models.CharField(max_length=8)
    isAtivo = models.CharField(max_length=12)
    funcaoFuncionarioId = models.CharField(max_length=6)
    departamentoId = models.CharField(max_length=6)

    def __str__(self):
        return self.nome
