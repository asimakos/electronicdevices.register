
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Authority(models.Model):
    
    name=models.CharField(verbose_name='ΔΙΕΥΘΥΝΣΗ',max_length=600)
    
    def __unicode__(self):
    
        return u'%s'% self.name    
