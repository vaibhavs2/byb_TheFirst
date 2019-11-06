from django.contrib import admin
from cart.models import Order, OrderItem
# Register your models here.
class OrderItemAdmin (admin.ModelAdmin):
    list_display = ('user','product','is_ordered')
    search_fields = ['user__username', 'product__book_name', 'is_ordered']

class OrderAdmin (admin.ModelAdmin):
    list_display = ('user','ref_code','ordered_date','is_ordered','payment_received','total_price','shipping_address')
    search_fields = ['ref_code','user__username','is_ordered']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)