from django.db import models
from atracao.models import Atracao
from comentarios.models import Comentarios
from avaliacao.models import Avaliacao
from enderecos.models import Enderecos


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Enderecos, on_delete=models.CASCADE,
                                 null=True, blank=True)

    def __str__(self):
        return self.nome
