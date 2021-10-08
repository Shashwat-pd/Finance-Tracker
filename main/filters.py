import django_filters
from .models import *

class IncomeFilter(django_filters.FilterSet):
    class Meta:
        model = IncomeItem
        fields = '__all__'

class ExpenditureFilter(django_filters.FilterSet):
    class Meta:
        model = ExpenditureItem
        fields = '__all__'
