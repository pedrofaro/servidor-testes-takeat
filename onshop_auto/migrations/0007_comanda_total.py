# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-08-25 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onshop_auto', '0006_auto_20190823_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='comanda',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]