# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response,render
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import RequestConfig
from django.http import HttpResponse
from django.template import RequestContext
from category.models import Category
from filters import CategoryFilter
from django_tables2 import SingleTableView
import category.tables as mytables
from django.contrib.auth import REDIRECT_FIELD_NAME
from easy_pdf.views import PDFTemplateView


# Create your views here.
class CategoryTableView(LoginRequiredMixin,SingleTableView):
    
    login_url = "/login/"
    #redirect_field_name= 
    
    def get_table_data(self):
        data = super(CategoryTableView, self).get_table_data()
        self.filter = CategoryFilter(self.request.GET, queryset=data)
        return self.filter        
    
    
    def get_context_data(self, **kwargs):
        context = super(CategoryTableView, self).get_context_data(**kwargs) 
       
        context['filter'] = self.filter
        context['search']=u'Αναζήτηση'
        context['clear']=u'Καθαρισμός'
        context['display']=u'Εμφάνιση'
        context['of']=u'από'
        context['items']=u'εγγραφές'
        
        return context    
    
    
class CategoryPDFView(PDFTemplateView):
    template_name = "pdf_category.html"
    
    def get(self,request,*args, **kwargs):
        context = self.get_context_data(pagesize="A4",title=u"Κατηγορία υλικού",**kwargs)
        self.query_results = Category.objects.get(id=kwargs['pk'])
        context["query_results"] = self.query_results
        return self.render_to_response(context)
    
    
class CategoryallPDFView(PDFTemplateView):
    template_name = "pdf_allcategory.html"

    def get(self,request,*args, **kwargs):
        context = self.get_context_data(pagesize="A4",title=u"Κατηγορίες",**kwargs)
        self.query_results = Category.objects.all()
        context["query_results"] = self.query_results
        return self.render_to_response(context) 
    
    
    
    