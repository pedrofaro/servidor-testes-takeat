# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-30 19:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onshop_core', '0007_pformaspag_pmesa_ppedidos_ppedidosformapag_pproduto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='endereco',
            field=models.TextField(default='Rua Tal'),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='horario_abertura',
            field=models.TimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='horario_fechamento',
            field=models.TimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
