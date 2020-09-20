from django.db import models
from django.contrib.auth.models import User

choice=(  
        ('I', "sem I"),
        ('II', "sem II"),
        ('III', "sem III"),
        ('IV', "sem IV"),
        ('V', "sem V"),
        ('VI', "sem VI"),('VII', "sem VII"),('VIII',"sem VIII"),)
        
class branch(models.Model):
    branches = models.CharField(max_length=100)
    def __str__(self):
        return self.branches
             
# Create your models here.
class GoodDeals(models.Model):
    semester = models.CharField(default='I', max_length=11, choices=choice)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    bookSets = models.BooleanField()
    priceTosell = models.FloatField()
    priceTOshow = models.FloatField()
    description = models.CharField(max_length=1000, null=True)
    ImageUrl = models.URLField(unique = True)
    InStock = models.SmallIntegerField(default=1)
    showing = models.BooleanField(default=True)

    def __str__(self):
        return self.branch.branches
        


class order_deals(models.Model):
    product = models.ForeignKey(GoodDeals, on_delete=models.CASCADE, null=True)
    adress = models.CharField(max_length=1000, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_received = models.BooleanField(default=False)
    is_ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(null=True)
    ref_code =models.CharField(max_length=20, null=True)
