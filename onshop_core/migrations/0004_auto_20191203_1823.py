# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-12-03 21:23
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onshop_core', '0003_auto_20191203_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='pedido_minimo',
            field=models.DecimalField(decimal_places=2, default=Decimal('10.00'), max_digits=8, null=True),
        ),
    ]
