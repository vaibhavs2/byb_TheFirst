from django.db import models
from users.models import Profile
from product.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from theFirst.models import GoodDeals
from django.utils.timezone import now
from django.shortcuts import reverse

# Create your models here.


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,null=True )
    is_ordered = models.BooleanField(default=False)
    added_date = models.DateTimeField(default=now, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return  f"{self.product.book_name}  |  {self.product.id} | {self.product.semester} | {self.product.branch} | {self.product.year_of_book}"



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    ref_code = models.CharField(max_length=20, null=True)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(null=True)
    is_ordered = models.BooleanField(default=False)
    shipping_address = models.CharField(max_length=1000, null=True)
    total_price = models.PositiveIntegerField(editable=False,default = 0)
    # payment = models.ForeignKey(
    #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    # being_delivered = models.BooleanField(default=False)
    payment_received = models.BooleanField(default=False)
    # refund_requested = models.BooleanField(default=False)
    # refund_granted = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        try:
            return sum([item.product.price for item in self.items.all()])
        except KeyError:
            return 0 

    def __str__(self):
        return '{0} - {1}'.format(self.user.username, self.ref_code)
