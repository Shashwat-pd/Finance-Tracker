
from django.views.generic import TemplateView
from main.models import ExpenditureItem, IncomeItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now
from datetime import date



# Create your views here.
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


    def get_context_data(self, **kwargs):
        total_income_month = 0
        income_items = IncomeItem.objects.filter(user=self.request.user)

        this_month_start = date.today().replace(day= 1)
        this_month_now = date.today()

        income_items_month = income_items.filter(transaction_date__gte=this_month_start, transaction_date__lte=this_month_now)

        for i in income_items_month:
            total_income_month = total_income_month + i.amount

        total_expenditure_month = 0
        expenditure_items = ExpenditureItem.objects.filter(user=self.request.user)

        expenditure_items_month = expenditure_items.filter(transaction_date__gte=this_month_start, transaction_date__lte=this_month_now)

        for i in expenditure_items_month:
            total_expenditure_month = total_expenditure_month + i.amount

        net = total_income_month - total_expenditure_month
        
        context = super().get_context_data(**kwargs)
        context["total_income_month"] = total_income_month
        context["total_expenditure_month"] = total_expenditure_month
        context["income_items"] = reversed(income_items)
        context["expenditure_items"] = reversed(expenditure_items)
        context["net"] = net

        return context




    
    

