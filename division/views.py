# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response,render
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import RequestConfig
from django.http import HttpResponse
from django.template import RequestContext
from division.models import Division
from filters import DivisionFilter
from django_tables2 import SingleTableView
import category.tables as mytables
from easy_pdf.views import PDFTemplateView

# Create your views here.
class DivisionTableView(LoginRequiredMixin,SingleTableView):
    
    login_url = '/login/'
    #redirect_field_name=request.GET(self.redirect_field_name)    
    
    def get_table_data(self):
        data = super(DivisionTableView, self).get_table_data()
        self.filter = DivisionFilter(self.request.GET, queryset=data)
        return self.filter        
    
    
    def get_context_data(self, **kwargs):
        context = super(DivisionTableView, self).get_context_data(**kwargs) 
       
        context['filter'] = self.filter
        context['search']=u'Αναζήτηση'
        context['clear']=u'Καθαρισμός'
        context['display']=u'Εμφάνιση'
        context['of']=u'από'
        context['items']=u'εγγραφές'        
        
        return context  
    
    
class DivisionPDFView(PDFTemplateView):
    template_name = "pdf_division.html"

    def get(self,request,*args, **kwargs):
        context = self.get_context_data(pagesize="A4",title=u"Τμήμα",**kwargs)
        self.query_results = Division.objects.get(id=kwargs['pk'])
        context["query_results"] = self.query_results
        return self.render_to_response(context)     
    
    
class DivisionallPDFView(PDFTemplateView):
    template_name = "pdf_alldivision.html"

    def get(self,request,*args, **kwargs):
        context = self.get_context_data(pagesize="A4",title=u"Τμήματα",**kwargs)
        self.query_results = Division.objects.all()
        context["query_results"] = self.query_results
        return self.render_to_response(context)         
    