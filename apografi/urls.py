"""apografi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include,patterns
from apografi.settings import STATIC_ROOT
from django.db import models
from category.models import Category
from authority.models import Authority
from division.models import Division
from employee.models import Employee
from article.models import Article
import category.tables as categorytables
import division.tables as divisiontables
import authority.tables as authoritytables
import employee.tables as employeetables
import article.tables as articletables
from category.views import CategoryTableView
from category.views import CategoryPDFView
from category.views import CategoryallPDFView
from authority.views import AuthorityTableView
from division.views import DivisionTableView
from employee.views import EmployeeTableView
from article.views import ArticleTableView
from division.views import DivisionPDFView
from division.views import DivisionallPDFView
from authority.views import AuthorityPDFView
from authority.views import AuthorityallPDFView
from employee.views import EmployeePDFView
from employee.views import EmployeeallPDFView
from article.views import ArticlePDFView
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required



urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^login/$', 'apografi.views.login',name="user_login"),
      url(r'^logout/$', 'apografi.views.logout_view',name="user_logout"),
     url(r'^auth/$', 'apografi.views.auth_view'),
     url(r'^loggedIn/', 'apografi.views.loggedin'),
     url(r'^invalid/', 'apografi.views.invalid'),
    url(r'^division/$', DivisionTableView.as_view(
        model=Division,
        table_class=divisiontables.DivisionTable,
        template_name ='division.html', 
        table_pagination={"per_page":20 }),
        name="list_division"
        ),        
    url(r'^authority/$', AuthorityTableView.as_view(
        model=Authority,
        table_class=authoritytables.AuthorityTable,
        template_name ='authority.html', 
        table_pagination={"per_page":20 }),
        name="list_authority"
        ),    
    url(r'^category/$', CategoryTableView.as_view(
        model=Category,
        table_class=categorytables.CategoryTable,
        template_name ='category.html', 
        table_pagination={"per_page":20 }),
        name="list_category"
    ),
    url(r'^employee/$', EmployeeTableView.as_view(
        model=Employee,
        table_class=employeetables.EmployeeTable,
        template_name ='employee.html', 
        table_pagination={"per_page":20 }),
        name="list_employee"
        ), 
    url(r'^article/$', ArticleTableView.as_view(
        model=Article,
        table_class=articletables.ArticleTable,
        template_name ='article.html', 
        table_pagination={"per_page":20 }),
        name="list_article"
        ),        
    url(r'^crud/',  include('crudbuilder.urls')),
    url(r'^crud/category/categories/create$',RedirectView.as_view(),name="create_category"),    
    url(r'^category/update/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/category/categories/%(pk)s/update'),name="edit_category"), 
    url(r'^category/delete/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/category/categories/%(pk)s/delete'),name="delete_category"), 
    url(r'^category/view/(?P<pk>(\d+))/category.pdf$',CategoryPDFView.as_view(),name="view_category"),
    url(r'^category/view/allcategory.pdf$',CategoryallPDFView.as_view(),name="view_allcategory"),
    url(r'^authority/update/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/authority/authorities/%(pk)s/update'),name="edit_authority"), 
    url(r'^authority/delete/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/authority/authorities/%(pk)s/delete'),name="delete_authority"),
    url(r'^authority/view/(?P<pk>(\d+))/authority.pdf$',AuthorityPDFView.as_view(),name="view_authority"),
    url(r'^authority/view/allauthority.pdf$',AuthorityallPDFView.as_view(),name="view_allauthority"),
    url(r'^division/update/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/division/divisions/%(pk)s/update'),name="edit_division"), 
    url(r'^division/delete/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/division/divisions/%(pk)s/delete'),name="delete_division"), 
    url(r'^division/view/(?P<pk>(\d+))/division.pdf$',DivisionPDFView.as_view(),name="view_division"),
    url(r'^division/view/alldivision.pdf$',DivisionallPDFView.as_view(),name="view_alldivision"),
    url(r'^employee/update/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/employee/employees/%(pk)s/update'),name="edit_employee"), 
    url(r'^employee/delete/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/employee/employees/%(pk)s/delete'),name="delete_employee"), 
    url(r'^employee/view/(?P<pk>(\d+))/employee.pdf$',EmployeePDFView.as_view(),name="view_employee"),
    url(r'^article/update/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/article/articles/%(pk)s/update'),name="edit_article"), 
    url(r'^article/delete/(?P<pk>(\d+))/$',RedirectView.as_view(
        url='/crud/article/articles/%(pk)s/delete'),name="delete_article"),
    url(r'^article/view/(?P<pk>(\d+))/article.pdf$',ArticlePDFView.as_view(),name="view_article"),
    url(r'^employee/view/allemployee.pdf$',EmployeeallPDFView.as_view(),name="view_allemployee"),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes' : True}),
]

#urlpatterns += patterns('', url(r'^grid_json/', include(djqgrid.urls)))



