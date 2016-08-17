
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from authority.models import Authority
from division.models import Division

# Create your models here.

class Employee(models.Model):
    
    name=models.CharField(verbose_name='ΟΝΟΜΑΤΕΠΩΝΥΜΟ',max_length=800)
    authority=models.ForeignKey(Authority,verbose_name='ΔΙΕΥΘΥΝΣΗ')
    division=models.ForeignKey(Division,verbose_name='ΤΜΗΜΑ')
        
    def __unicode__(self):
        
        return u'%s'% self.name        
