
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from authority.models import Authority

# Create your models here.

class Division(models.Model):
    
    name=models.CharField(verbose_name='ΤΜΗΜΑ',max_length=800)
    authority=models.ForeignKey(Authority,verbose_name='ΔΙΕΥΘΥΝΣΗ')
    
    def __unicode__(self):
    
        return u'%s'% self.name    
