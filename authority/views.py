
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response,render
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import RequestConfig
from django.http import HttpResponse
from django.template import RequestContext
from authority.models import Authority
from filters import AuthorityFilter
from django_tables2 import SingleTableView
import authority.tables as mytables
from easy_pdf.views import PDFTemplateView

# Create your views here.
class AuthorityTableView(LoginRequiredMixin,SingleTableView):
    
    login_url = '/login/'
    #redirect_field_name=request.GET(self.redirect_field_name)    
    
    def get_table_data(self):
        data = super(AuthorityTableView, self).get_table_data()
        self.filter = AuthorityFilter(self.request.GET, queryset=data)
        return self.filter        
    
    
    def get_context_data(self, **kwargs):
        context = super(AuthorityTableView, self).get_context_data(**kwargs) 
       
        context['filter'] = self.filter
        context['search']=u'Αναζήτηση'
        context['clear']=u'Καθαρισμός'
        context['display']=u'Εμφάνιση'
        context['of']=u'από'
        context['items']=u'εγγραφές'        
        
        return context   
    
    
class AuthorityPDFView(PDFTemplateView):
    template_name = "pdf_authority.html"

    def get(self,request,*args, **kwargs):
        context = self.get_context_data(pagesize="A4",title=u"Διεύθυνση",**kwargs)
        self.query_results = Authority.objects.get(id=kwargs['pk'])
        context["query_results"] = self.query_results
        return self.render_to_response(context)   
    

class AuthorityallPDFView(PDFTemplateView):
    template_name = "pdf_allauthority.html"

    def get(self,request,*args, **kwargs):
        context = self.get_context_data(pagesize="A4",title=u"Διευθύνσεις",**kwargs)
        self.query_results = Authority.objects.all()
        context["query_results"] = self.query_results
        return self.render_to_response(context)        