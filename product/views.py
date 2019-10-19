from django.shortcuts import render
from product.models import Product
# Create your views here.


def product_view(request):
    context = {
                'products' : Product.objects.all() , }
    return render(request,'product/product_view.html', context=context) 