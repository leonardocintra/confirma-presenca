# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convidado', '0004_convidado_mensagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaConvidados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_convidado', models.CharField(max_length=300, unique=True)),
                ('quantidade_convidados', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'lista_convidados',
            },
        ),
    ]
