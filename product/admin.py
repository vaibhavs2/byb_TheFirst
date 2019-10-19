from django.contrib import admin
from product.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_product = ('book_name','semester','year_of_book', 'branch','stock','status_new',)


admin.site.register(Product , ProductAdmin)