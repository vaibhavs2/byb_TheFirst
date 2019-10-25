from django.contrib import admin
from .models import Profile, UserOrders


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name','number','city','address','landmark','pinCode')

class userOrderAdmin(admin.ModelAdmin):
    list_display = ('product_id','user','price','order_Date','deliver_status',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserOrders,userOrderAdmin )
