from django.contrib import admin
from sell.models import sell_order, stock
# Register your models here.
class sell_orderAdmin(admin.ModelAdmin):
    list_display = ('selling_user','date_recv','price', 'semester', 'branch', 'book_name', 'year_of_book','number', 'address', 'landmark', 'city', 'pinCode',)
    search_fields = ['selling_user__username', 'date_recv', 'branch__branches', 'semester','pinCode', 'city']

class stockAdmin (admin.ModelAdmin):
    list_display = ('branch','semester','stock_need')
    search_fields = ['branch__branches', 'semester']
 
admin.site.register(sell_order, sell_orderAdmin)
admin.site.register(stock, stockAdmin)