
from crudbuilder.abstract import BaseCrudBuilder
from models import Category

class CategoryCrud(BaseCrudBuilder):
    
    model = Category
    search_feilds = ['name']
    tables2_fields = ('name',)
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    #modelform_excludes = ['created_by', 'updated_by']
    login_required=True
    permission_required=False
    
    custom_templates = {
        'list': 'category/list.html',
        'create': 'category/create.html',
        'detail': 'category/detail.html',
        'update': 'category/update.html',
        'delete': 'category/delete.html'
    }    