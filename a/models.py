# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class B(models.Model):
    charfield = models.CharField(max_length=1, default='', db_index=False)
    intfield = models.IntegerField(default=0, db_index=False)


class C(models.Model):
    b = models.ForeignKey(B, db_index=False)
