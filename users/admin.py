from django.contrib import admin
from .models import Profile, UserOrders


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name','number','city','address','landmark','pinCode')
    search_fields = ['user', 'name', 'number', 'pinCode']

class userOrderAdmin(admin.ModelAdmin):
    list_display = ('product_id','user','price','order_Date','deliver_status',)
    search_fields = ['product_id', 'user__username']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserOrders,userOrderAdmin )
