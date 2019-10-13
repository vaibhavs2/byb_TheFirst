from django.db import models
from django.contrib.auth.models import User
# Create your models here.

choice = (
    ('Bhilai','Bhilai'),('Durg', 'Durg'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=10,null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    landmark = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=40, choices=choice, null=True, blank=True)
    pinCode = models.CharField(null=True, max_length=6,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

