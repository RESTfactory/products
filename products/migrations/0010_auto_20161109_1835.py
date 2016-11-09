# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20161109_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='price_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.PriceType'),
            preserve_default=False,
        ),
    ]
