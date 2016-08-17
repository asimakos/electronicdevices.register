
from crudbuilder.abstract import BaseCrudBuilder
from models import Authority

class AuthorityCrud(BaseCrudBuilder):
    
    model = Authority
    search_feilds = ['name']
    tables2_fields = ('name',)
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    #modelform_excludes = ['created_by', 'updated_by']
    login_required=True
    permission_required=False
    
    custom_templates = {
        'list': 'authority/list.html',
        'create': 'authority/create.html',
        'detail': 'authority/detail.html',
        'update': 'authority/update.html',
        'delete': 'authority/delete.html'
    }        