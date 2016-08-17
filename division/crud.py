
from crudbuilder.abstract import BaseCrudBuilder
from models import Division

class AuthorityCrud(BaseCrudBuilder):
    
    model = Division
    search_feilds = ['name']
    tables2_fields = ('name','authority')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    #modelform_excludes = ['created_by', 'updated_by']
    login_required=True
    permission_required=False
    
    custom_templates = {
        'list': 'division/list.html',
        'create': 'division/create.html',
        'detail': 'division/detail.html',
        'update': 'division/update.html',
        'delete': 'division/delete.html'
    }        