from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import DeleteView
from main.models import IncomeItem
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import IncomeFilter

from datetime import date, timedelta

# Create your views here.
class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = IncomeItem
    template_name = 'income_new.html'
    fields = ['title', 'category', 'amount', 'transaction_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IncomeCreateView, self).form_valid(form)


class IncomeDetail(LoginRequiredMixin, TemplateView):
    template_name = 'income_detail.html'

    def get_context_data(self, **kwargs):
        total_income = 0
        income_items = IncomeItem.objects.filter(user=self.request.user)

        myFilter = IncomeFilter(self.request.GET, queryset=income_items)
        income_items = myFilter.qs

        this_month = date.today().replace(day= 1)
        prev_month = (this_month - timedelta(days=15)).replace(day=1)

        last_month_items = IncomeItem.objects.filter(user=self.request.user).filter(transaction_date__gte=prev_month, transaction_date__lte=this_month)


        for i in IncomeItem.objects.filter(user= self.request.user):
            total_income = total_income + i.amount

        total_amount_filter = 0
        for i in income_items:
            total_amount_filter = total_amount_filter + i.amount

        last_month_income = 0
        for i in last_month_items:
            last_month_income = last_month_income + i.amount

        context = super().get_context_data(**kwargs)
        context["total_income"] = total_income
        context["income_items"] = reversed(income_items)
        context["myFilter"] = myFilter
        context["last_month_income"] = last_month_income
        context["total_amount_filter"] = total_amount_filter


        return context 


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = IncomeItem
    template_name = 'delete.html'    
    success_url = reverse_lazy('income_detail')