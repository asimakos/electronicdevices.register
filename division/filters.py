
import django_filters
from django.db import models
from models import Division


class DivisionFilter(django_filters.FilterSet):
    class Meta:
        model = Division
        fields = {
            'name': ['icontains']
            }        