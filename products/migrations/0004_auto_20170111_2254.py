# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 22:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',)},
        ),
    ]