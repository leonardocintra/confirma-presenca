# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convidado', '0003_auto_20170717_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='convidado',
            name='mensagem',
            field=models.TextField(blank=True, null=True),
        ),
    ]