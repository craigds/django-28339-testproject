# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c',
            name='b',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='a.B'),
        ),
    ]
