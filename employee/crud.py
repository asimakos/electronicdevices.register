
from crudbuilder.abstract import BaseCrudBuilder
from models import Employee

class EmployeeCrud(BaseCrudBuilder):
    
    model = Employee
    search_feilds = ['name']
    tables2_fields = ('name','authority','division')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    #modelform_excludes = ['created_by', 'updated_by']
    login_required=True
    permission_required=False
    
    custom_templates = {
        'list': 'employee/list.html',
        'create': 'employee/create.html',
        'detail': 'employee/detail.html',
        'update': 'employee/update.html',
        'delete': 'employee/delete.html'
    }        