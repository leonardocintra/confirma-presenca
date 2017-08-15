"""
    Convidado Model
"""
from django.db import models

CONFIRMA_PRESENCA = (
    ('SIM', 'Sim'),
    ('NAO', 'Não'),
)

CONVIDADO_POR = (
    ('NO', 'Noivo'),
    ('NA', 'Noiva'),
)

class Convidado(models.Model):
    """ Convidado - Model - Os convidados confirmam a presença aqui"""
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


class ListaConvidados(models.Model):
    """ Sua lista de casamento para controle """
    nome_convidado = models.CharField(max_length=300)
    quantidade_convidados = models.IntegerField(default=0)
    convidado_por = models.CharField('Convidado por', max_length=2, choices=CONVIDADO_POR)
    presenca_confirmada = models.BooleanField('Presença confirmada', default=False)

    def __str__(self):
        return self.nome_convidado

    class Meta:
        db_table = 'lista_convidados'