# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-25 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onshop_core', '0010_auto_20200525_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='link_picpay',
            field=models.CharField(default='#', max_length=200),
        ),
    ]
