# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convidado', '0007_auto_20170717_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaconvidados',
            name='presenca_confirmada',
            field=models.BooleanField(default=False, verbose_name='Presença confirmada'),
        ),
    ]
