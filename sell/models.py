from django.db import models
from theFirst.models import branch, choice
import datetime
from users.models import choice as city_choice
from django.contrib.auth.models import User



year_choices = tuple((i,)*2 for i in range(datetime.date.today().year-3, datetime.date.today().year+1))



def current_year():
    return datetime.date.today().year

city_choices= (('','--choose please, its limited for now--'),) + city_choice

class sell_order(models.Model):
    selling_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_recv = models.DateField(auto_now=True)
    semester = models.CharField(choices=choice,default='I', max_length=11)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=300)
    year_of_book = models.SmallIntegerField( choices=year_choices, default=current_year)
    number = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=400, null=True)
    landmark = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=60, choices=city_choices, null=True)
    pinCode = models.CharField(null=True, max_length=6)
    price = models.SmallIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.selling_user.username

class stock(models.Model):
    branch = models.ForeignKey(branch, on_delete= models.CASCADE)
    semester = models.CharField(choices=choice,default='I', max_length=11)
    stock_need = models.BooleanField(default=True)
    def  __str__ (self):
        return self.branch.branches
    class Meta:
        unique_together = ('branch', 'semester',)
