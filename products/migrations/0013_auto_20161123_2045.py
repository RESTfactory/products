# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 20:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20161115_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdata',
            name='local',
        ),
        migrations.RemoveField(
            model_name='productdata',
            name='product_instance',
        ),
        migrations.RemoveField(
            model_name='productdata',
            name='provision',
        ),
        migrations.RemoveField(
            model_name='productdata',
            name='status',
        ),
        migrations.DeleteModel(
            name='ProductData',
        ),
    ]
