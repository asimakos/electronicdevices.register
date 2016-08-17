
import django_filters
from django.db import models
from models import Employee


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
            'name': ['icontains']
            }        