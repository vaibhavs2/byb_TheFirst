from django.db import models
from theFirst.models import choice as sem_choice
from theFirst.models import branch
# Create your models here.

class Product(models.Model):
    image_url = models.CharField(max_length=2000)
    price = models.FloatField()
    stock = models.IntegerField()
    book_name = models.CharField(max_length=255)
    status_new = models.BooleanField(default=True) 
    year = models.ForeignKey
    semester = models.CharField(choices=sem_choice, default='I',max_length=11)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)