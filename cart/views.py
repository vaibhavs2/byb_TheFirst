from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Order, OrderItem
# Create your views here.

@login_required()
def order_summary(request, **kwargs):
    context = {
        'order': Order.objects.filter(user=request.user, is_ordered=False)[0],
    }
    return render(request, 'cart/order_summary.html', context)



@login_required()
def delete_from_cart(request, itemId):
    item_to_delete = OrderItem.objects.filter(pk=itemId)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('cart:yo'))
