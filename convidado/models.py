"""
    Convidado Model
"""
from django.db import models

class Convidado(models.Model):
    """ Convidado - Model"""
    CONFIRMA_PRESENCA = (
        ('SIM', 'Sim'),
        ('NAO', 'Não'),
    )
    nome_convidado = models.CharField(max_length=300, unique=True)
    quantidade_convidados = models.IntegerField(default=0)
    confirma_presenca = models.CharField('Confirma presença', default=True, choices=CONFIRMA_PRESENCA, max_length=3)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField(blank=True, null=True)

    def __str__ (self):
        """ str """
        return self.nome_convidado

    class Meta:
        """ Meta """
        db_table = 'convidados'
