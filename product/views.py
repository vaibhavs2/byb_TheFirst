from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.


# def product_view(request):
#     context = {
#                 'products' : Product.objects.all() , }
#     return render(request,'product/product_view.html', context=context) 

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_view.html'
    context_object_name = 'products'
    ordering = ['?', ]
    paginate_by = 20
    

    # def get_queryset(self):
    # return Product.objects.filter(user=self.request.user.)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

# def product_detail(request):
#     return render(request, 'product/product_detail.html') 

