# -*- coding: utf-8 -*-

import django_tables2 as tables
from django.db import models
from models import Division


class DivisionTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{% url "edit_division" record.pk %}"><img src=\'{% load  staticfiles %} {% static "images/edit.jpg" %}\' / width="25"></a>',verbose_name=u'Επεξεργασία',) 
    delete = tables.TemplateColumn('<a href="{% url "delete_division" record.pk %}"><img src=\'{% load  staticfiles %} {% static "images/delete.jpg" %}\' / width="25"></a>',verbose_name=u'Διαγραφή',)  
    view = tables.TemplateColumn('<a href="{% url "view_division" record.pk %}"><img src=\'{% load  staticfiles %} {% static "images/view.jpg" %}\' / width="25"></a>',verbose_name=u'Επισκόπηση',) 
    class Meta:
        model=Division
        attrs = {"class":"paleblue table table-striped table-condensed table-bordered"}