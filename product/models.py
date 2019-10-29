from django.db import models
from theFirst.models import choice as sem_choice
from theFirst.models import branch
from sell.models import current_year
import datetime
# Create your models here.
year_choices = tuple((i,)*2 for i in range(datetime.date.today().year-3, datetime.date.today().year+1))

class Product(models.Model):
    image_url = models.CharField(max_length=2000)
    image_url1 = models.CharField(max_length=2000, blank=True, null=True)
    image_url2= models.CharField(max_length=2000, blank=True, null=True)
    price = models.FloatField()
    price_toshow = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()
    book_name = models.CharField(max_length=255)
    status_new = models.BooleanField(default=True) 
    year_of_book = models.SmallIntegerField( choices=year_choices, default=current_year)
    semester = models.CharField(choices=sem_choice, default='I',max_length=11)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.book_name
        
class bestSelling(models.Model):
    books = models.OneToOneField(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.books.book_name



    