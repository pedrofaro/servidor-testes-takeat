# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2020-04-26 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onshop_auto', '0024_formapagamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conciliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_pago', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('comanda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='onshop_auto.Comanda')),
                ('forma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onshop_auto.FormaPagamento')),
            ],
        ),
    ]
