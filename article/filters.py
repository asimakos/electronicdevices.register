
# -*- coding: utf-8 -*-

import django_filters
from django.db import models
from models import Article


class ArticleFilter(django_filters.FilterSet):
    employee__name = django_filters.CharFilter(label=u'ΠΡΟΣΩΠΙΚΟ',lookup_type='icontains')
    authority__name = django_filters.CharFilter(label=u'ΔΙΕΥΘΥΝΣΗ',lookup_type='icontains')
    class Meta:
        model = Article
        fields = {
            'marka': ['icontains'],
            'montelo': ['icontains'],
            'seiriakos': ['icontains'],
            'num_apografis': ['icontains']
            }  
       