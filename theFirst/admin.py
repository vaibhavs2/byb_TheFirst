from django.contrib import admin
from theFirst.models import GoodDeals, branch, order_deals

class GoodDealsAdmin(admin.ModelAdmin):
    list_display = ('id','semester','branch','bookSets', 'priceTosell','InStock', 'priceTOshow', 'showing')
    search_fields = ['id',]

class branchAdmin(admin.ModelAdmin):
    list_display = ('branches',)

class order_dealAdmin(admin.ModelAdmin):
    list_display=('product__id','ref_code','user','ordered_date','payment_received','is_ordered', 'adress')

admin.site.register(branch,branchAdmin)
admin.site.register(GoodDeals, GoodDealsAdmin)
admin.site.register(order_deals)

