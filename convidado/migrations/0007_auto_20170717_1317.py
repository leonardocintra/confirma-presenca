# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convidado', '0006_listaconvidados_convidado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaconvidados',
            name='nome_convidado',
            field=models.CharField(max_length=300),
        ),
    ]
