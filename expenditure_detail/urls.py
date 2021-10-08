from django.urls.conf import path

from expenditure_detail.views import ExpenditureDetail, DeleteItem

urlpatterns = [
    path('', ExpenditureDetail.as_view(), name='expenditure_detail'),
    path('delete/<int:pk>', DeleteItem.as_view(), name='expenditure_delete')

]
