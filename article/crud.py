

from crudbuilder.abstract import BaseCrudBuilder
from models import Article

class ArticleCrud(BaseCrudBuilder):
    
    model = Article
    search_feilds = ['marka','montelo','seiriakos','num_apografis','employee__name']
    tables2_fields = ('marka','montelo','seiriakos','leitourgiko','num_apografis','sxolia','category','employee','authority')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    #modelform_excludes = ['created_by', 'updated_by']
    login_required=True
    permission_required=False
    
    custom_templates = {
        'list': 'article/list.html',
        'create': 'article/create.html',
        'detail': 'article/detail.html',
        'update': 'article/update.html',
        'delete': 'article/delete.html'
    }        