# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response,render
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import RequestConfig
from django.http import HttpResponse
from django.template import RequestContext
from employee.models import Employee
from filters import EmployeeFilter
from django_tables2 import SingleTableView
import employee.tables as mytables
from easy_pdf.views import PDFTemplateView

# Create your views here.
class EmployeeTableView(LoginRequiredMixin,SingleTableView):
    
    login_url = '/login/'
    #redirect_field_name=request.GET(self.redirect_field_name)    
    
    def get_table_data(self):
        data = super(EmployeeTableView, self).get_table_data()
        self.filter = EmployeeFilter(self.request.GET, queryset=data)
        return self.filter        
    
    
    def get_context_data(self, **kwargs):
        context = super(EmployeeTableView, self).get_context_data(**kwargs) 
       
        context['filter'] = self.filter
        context['search']=u'Αναζήτηση'
        context['clear']=u'Καθαρισμός'
        context['display']=u'Εμφάνιση'
        context['of']=u'από'
        context['items']=u'εγγραφές'
        
        return context    
    
    
class EmployeePDFView(PDFTemplateView):
    template_name = "pdf_employee.html"
    
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(pagesize="A4",title=u"Προσωπικό - Υπάλληλος",**kwargs)
        self.query_results = Employee.objects.get(id=kwargs['pk'])
        context["query_results"] = self.query_results
        return self.render_to_response(context)
    
    
class EmployeeallPDFView(PDFTemplateView):
    template_name = "pdf_allemployee.html"

    def get(self,request,*args,**kwargs):
        context = self.get_context_data(pagesize="A4",title=u"Προσωπικό - Υπάλληλοι",**kwargs)
        self.query_results = Employee.objects.all()
        context["query_results"] = self.query_results
        return self.render_to_response(context)     
