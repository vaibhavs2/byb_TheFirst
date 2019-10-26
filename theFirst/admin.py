from django.contrib import admin
from theFirst.models import GoodDeals, branch

class GoodDealsAdmin(admin.ModelAdmin):
    list_display = ('semester','branch','bookSets', 'priceTosell','InStock', 'priceTOshow','TimeLimit')
class branchAdmin(admin.ModelAdmin):
    list_display = ('branches',)

    
admin.site.register(branch,branchAdmin)
admin.site.register(GoodDeals, GoodDealsAdmin)

