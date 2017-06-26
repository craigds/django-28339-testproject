# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class B(models.Model):
    pass


class C(models.Model):
    b = models.ForeignKey(B, db_index=False)
