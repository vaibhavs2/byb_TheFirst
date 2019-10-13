from django.contrib import admin
from theFirst.models import GoodDeals, bestSelling, branch

class GoodDealsAdmin(admin.ModelAdmin):
    list_display = ('semester','branch','bookSets', 'priceTosell','InStock', 'priceTOshow','TimeLimit')
class bestSellingAdmin(admin.ModelAdmin):
    list_display = ('branch', 'semester','bookName','bookPrice','InStock','newedition')
class branchAdmin(admin.ModelAdmin):
    list_display = ('branches',)

    
admin.site.register(branch,branchAdmin)
admin.site.register(GoodDeals, GoodDealsAdmin)
admin.site.register(bestSelling, bestSellingAdmin)
