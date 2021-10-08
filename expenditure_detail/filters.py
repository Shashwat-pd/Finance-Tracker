import django_filters
from django_filters.filters import RangeFilter

from main.models import ExpenditureItem

class ExpenditureFilter(django_filters.FilterSet):
    amount = RangeFilter()

    class Meta:
        model = ExpenditureItem
        fields = '__all__'
        exclude = ['user', 'transaction_date', 'amount']
