from django.urls import path
from django.urls.conf import include
from .views import HomePageView
from income_detail.views import IncomeCreateView, IncomeDetail
from expenditure_detail.views import ExpenditureCreateView, ExpenditureDetail



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add_income/', IncomeCreateView.as_view(), name='add_income'),
    path('add_expenditure/', ExpenditureCreateView.as_view(), name='add_expenditure'),
    path('expenditure_detail/', include('expenditure_detail.urls')),
    path('income_detail/', include('income_detail.urls')),
]
