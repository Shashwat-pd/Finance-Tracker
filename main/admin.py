from django.contrib import admin
from .models import IncomeItem, ExpenditureItem

# Register your models here.
admin.site.register(IncomeItem)
admin.site.register(ExpenditureItem)

