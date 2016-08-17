
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from authority.models import Authority
from category.models import Category
from employee.models import Employee

# Create your models here.

class Article(models.Model):
    
    marka=models.CharField(verbose_name='ΜΑΡΚΑ',max_length=300)
    montelo=models.CharField(verbose_name='ΜΟΝΤΕΛΟ',max_length=300)
    seiriakos=models.CharField(verbose_name='ΣΕΙΡΙΑΚΟΣ',max_length=300)
    leitourgiko=models.CharField(verbose_name='ΛΕΙΤΟΥΡΓΙΚΟ',max_length=100)
    num_apografis=models.CharField(verbose_name='ΚΩΔΙΚΟΣ ΛΕΙΤΟΥΡΓΙΚΟΥ',max_length=200)
    sxolia=models.CharField(verbose_name='ΠΑΡΑΤΗΡΗΣΕΙΣ',max_length=300)
    
    authority=models.ForeignKey(Authority,verbose_name='ΔΙΕΥΘΥΝΣΗ')
    category=models.ForeignKey(Category,verbose_name='ΚΑΤΗΓΟΡΙΑ')
    employee=models.ForeignKey(Employee,verbose_name='ΠΡΟΣΩΠΙΚΟ')
        
    def __unicode__(self):
        
        return u'%s %s'% (self.marka,self.montelo)       
