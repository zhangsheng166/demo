# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-21 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='area',
            field=models.CharField(default='', max_length=50, verbose_name='地区'),
        ),
    ]
