from django.urls.conf import path

from .views import DeleteItem, IncomeDetail

urlpatterns = [
    path('', IncomeDetail.as_view(), name='income_detail'),
    path('income_delete/<int:pk>', DeleteItem.as_view(), name='delete')
]

