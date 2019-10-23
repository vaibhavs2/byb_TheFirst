from django.contrib import admin
from product.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('book_name','branch','semester','year_of_book','price' ,'stock','status_new',)

admin.site.register(Product , ProductAdmin)