# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response,render
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import RequestConfig
from django.http import HttpResponse
from django.template import RequestContext
from article.models import Article
from filters import ArticleFilter
from django_tables2 import SingleTableView
import article.tables as mytables
from easy_pdf.views import PDFTemplateView

# Create your views here.
class ArticleTableView(LoginRequiredMixin,SingleTableView):
    
    login_url = '/login/'
    #redirect_field_name=request.GET(self.redirect_field_name)    
    
    def get_table_data(self):
        data = super(ArticleTableView, self).get_table_data()
        self.filter = ArticleFilter(self.request.GET, queryset=data)
        return self.filter        
    
    
    def get_context_data(self, **kwargs):
        context = super(ArticleTableView, self).get_context_data(**kwargs) 
       
        context['filter'] = self.filter
        context['search']=u'Αναζήτηση'
        context['clear']=u'Καθαρισμός'
        context['display']=u'Εμφάνιση'
        context['of']=u'από'
        context['items']=u'εγγραφές'
        
        return context 
    
    
class ArticlePDFView(PDFTemplateView):
    template_name = "pdf_article.html"
        
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(pagesize="A4",title=u"Υλικό",**kwargs)
        self.query_results = Article.objects.get(id=kwargs['pk'])
        context["query_results"] = self.query_results
        return self.render_to_response(context)       
    