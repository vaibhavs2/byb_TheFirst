from django.shortcuts import render, redirect , get_object_or_404
from django.views.generic import ListView, DetailView
from product.models import Product
from django.urls import reverse
from cart.models import OrderItem, Order
from django.conf import settings
from django.contrib.auth.decorators import login_required
import random
import string
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.


# def product_view(request):
#     context = {
#                 'products' : Product.objects.all() , }
#     return render(request,'product/product_view.html', context=context) 

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_view.html'
    context_object_name = 'products'
    ordering = ['-id']
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if self.request.user.is_authenticated:
            context['cart_listId'] = OrderItem.objects.filter(user=self.request.user, is_ordered=False).values_list('product_id',flat=True)
            
        else: 
            context['cart_listId']=OrderItem.objects.none()
        return context

    # def get_queryset(self):
    # return Product.objects.filter(user=self.request.user.)
def searchItems(request):
    context={}
    if request.method == 'GET':
        search_query = request.GET['searchBox']
        context={'products':Product.objects.filter(book_name__icontains=search_query),}
        
    return render(request, 'product/product_view.html',context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

# def product_detail(request):
#     return render(request, 'product/product_detail.html') 
def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))



@login_required
def add_to_cart(request):
    itemId = request.GET.get("itemId", None)
    product = Product.objects.filter(id = itemId).first()

    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(user=request.user, product=product, is_ordered=False)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(user=request.user, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = create_ref_code()
        user_order.save()
    list_Id = True
    data={
        "order":list_Id,
    }
    return JsonResponse(data)

