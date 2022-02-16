from django.db import models
import django_filters
from student.models import Activity

class ActivityFilter(django_filters.FilterSet):
    centre__centre_name = django_filters.CharFilter(lookup_expr='icontains')
    professor__professor_name = django_filters.CharFilter(lookup_expr= 'icontains')  
    class Meta:
        model = Activity
        fields =['centre__centre_name', 'professor__professor_name']