# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convidado', '0002_auto_20170717_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convidado',
            name='confirma_presenca',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NAO', 'Não')], default=True, max_length=3, verbose_name='Confirma presença'),
        ),
    ]
