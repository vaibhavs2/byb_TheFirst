from django.contrib import admin
from product.models import Product, bestSelling
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','book_name','branch','semester','year_of_book','price' ,'stock','status_new',)

class bestSellingAdmin(admin.ModelAdmin):
    model=bestSelling
    list_display = ('books_id','book_name', 'price', 'stock')

    def book_name(self, obj):
        return obj.books.book_name
    book_name.short_description = 'Product Name'

    def price(self, obj):
        return obj.books.semester
    price.short_description = 'price'

    def stock(self, obj):
        return obj.books.stock
    stock.short_description = 'stock'


admin.site.register(Product , ProductAdmin)

admin.site.register(bestSelling, bestSellingAdmin)
