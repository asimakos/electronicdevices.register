
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Category(models.Model):
    
    name=models.CharField(verbose_name='ΚΑΤΗΓΟΡΙΑ',max_length=300)
    
    def __unicode__(self):
        
        return u'%s'% self.name