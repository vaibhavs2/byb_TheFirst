from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save

# Create your models here.

choice = (
    ('Bhilai','Bhilai'),('Durg', 'Durg'))

numeric = RegexValidator(r'^([\s\d]+)$', 'Only numbers are allowed.')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=10, null=True, blank=True, validators=[numeric])
    address = models.CharField(max_length=400, null=True, blank=True)
    landmark = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=40, choices=choice, null=True, blank=True)
    pinCode = models.CharField(null=True, max_length=6,blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'


class UserOrders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.CharField(max_length=8, null=True)
    price = models.IntegerField(unique=False, null=True)
    order_Date = models.DateTimeField(null=True)
    deliver_status = models.BooleanField(default=False, null=True)
    def __str__(self):
        return f'{self.product_id}'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user = kwargs['instance'])
        user_order = UserOrders.objects.create(user = kwargs['instance'])
post_save.connect(create_profile, sender=User)