from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView
from main.models import ExpenditureItem
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import ExpenditureFilter
from datetime import date, timedelta


# Create your views here.
class ExpenditureCreateView(LoginRequiredMixin, CreateView):
    model = ExpenditureItem
    template_name = 'expenditure_new.html'
    fields = ['title', 'category', 'amount', 'transaction_date']


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExpenditureCreateView, self).form_valid(form)

class ExpenditureDetail(LoginRequiredMixin, TemplateView):
    template_name = 'expenditure_detail.html'

    def get_context_data(self, **kwargs):
    
        total_expenditure = 0
        expenditure_items = ExpenditureItem.objects.filter(user=self.request.user)

        for i in ExpenditureItem.objects.filter(user= self.request.user):
            total_expenditure = total_expenditure + i.amount

        myFilter = ExpenditureFilter(self.request.GET, queryset=expenditure_items)
        expenditure_items = myFilter.qs

        total_amount_filter = 0
        for i in expenditure_items:
            total_amount_filter = total_amount_filter + i.amount

        this_month = date.today().replace(day= 1)
        prev_month = (this_month - timedelta(days=15)).replace(day=1)

        last_month_items = ExpenditureItem.objects.filter(user=self.request.user).filter(transaction_date__gte=prev_month, transaction_date__lte=this_month)

        last_month_expenditure = 0
        for i in last_month_items:
            last_month_expenditure = last_month_expenditure + i.amount
        
        context = super().get_context_data(**kwargs)
        context["total_expenditure"] = total_expenditure
        context["expenditure_items"] = expenditure_items
        context["myFilter"] = myFilter
        context["total_amount_filter"] = total_amount_filter
        context["last_month_expenditure"] = last_month_expenditure
        
        return context

class DeleteItem(LoginRequiredMixin, DeleteView):
    model = ExpenditureItem
    template_name = 'delete.html'    
    success_url = reverse_lazy('expenditure_detail')