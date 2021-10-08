import django_filters
from django_filters.filters import RangeFilter

from main.models import IncomeItem

class IncomeFilter(django_filters.FilterSet):
    amount = RangeFilter()

    class Meta:
        model = IncomeItem
        fields = '__all__'
        exclude = ['user', 'transaction_date', 'amount']
