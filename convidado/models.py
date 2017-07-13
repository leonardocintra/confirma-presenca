from django.db import models

class Convidado(models.Model):
    nome_convidado = models.CharField(max_length=300)
    quantidade_convidados = models.IntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.nome_convidado

    class Meta:
        db_table = 'convidados'
