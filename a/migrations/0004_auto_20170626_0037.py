# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0003_auto_20170626_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b',
            name='charfield',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='b',
            name='intfield',
            field=models.IntegerField(default=0),
        ),
    ]