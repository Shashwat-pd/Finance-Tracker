from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
INCOME_CATEGORIES = [('Salary','Salary'),
            ('Freelance','Freelance'),
            ('Commission','Commission'),
            ('Interest','Interest'),
            ('Others','Others')]
            

EXPENDITURE_CATEGORIES = [('Entertainment','Entertainment'),
                            ('Fooding','Fooding'),
                            ('Housing','Housing'),
                            ('Insurance','Insurance'),
                            ('Insurance','Insurance'),
                            ('Insurance','Insurance'),
                            ('Others','Others'),]
                            

class IncomeItem(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(choices=INCOME_CATEGORIES,max_length=100)
    amount = models.IntegerField()
    transaction_date = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
         return self.pk
    

class ExpenditureItem(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(choices=EXPENDITURE_CATEGORIES, max_length=100)
    amount = models.IntegerField()
    transaction_date = models.DateField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
         return self.pk

    
