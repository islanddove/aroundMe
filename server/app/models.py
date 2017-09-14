# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# ^lol thanks Django

def Event(models.Model):
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    

