
import django_filters
from django.db import models
from models import Authority


class AuthorityFilter(django_filters.FilterSet):
    class Meta:
        model = Authority
        fields = {
            'name': ['icontains']
            }        