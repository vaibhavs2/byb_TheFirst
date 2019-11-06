from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView
from cart.models import Order, OrderItem
from users.registerForm import updateUserForm, updateEmail
from users.models import Profile
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from cart import checksum
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
# Create your views here.

@login_required()
def order_summary(request, **kwargs):
    try:
        context = {
            'order': Order.objects.get(user=request.user, is_ordered=False),
        }
    except ObjectDoesNotExist:
        context={
            'order':Order.objects.filter(user=request.user, is_ordered=False),
        }

    return render(request, 'cart/order_summary.html', context)



@login_required()
def delete_from_cart(request, itemId):
    try:
        item_to_delete = OrderItem.objects.get(pk=itemId)
        item_to_delete.product.stock +=1
        item_to_delete.product.save()
        item_to_delete.delete()
        messages.info(request, "Item has been deleted")
    except ObjectDoesNotExist:
        messages.info(request, "Error occured")
    return redirect(reverse('cart:yo'))


@login_required()
def order_confirmed(request):
    try:
        user_profile_detail = Profile.objects.get(user=request.user)
        change_in_order = Order.objects.get(user=request.user, is_ordered=False)
        change_in_order.total_price=change_in_order.get_cart_total()
        change_in_order.shipping_address = f"{user_profile_detail.name}> <{user_profile_detail.number}> <{request.user.email}> <{user_profile_detail.address}> <{user_profile_detail.landmark}> <{user_profile_detail.city}> <{user_profile_detail.pinCode}"
        change_in_order.ordered_date = datetime.now()
        change_in_order.save()
        for r in change_in_order.get_cart_items():
            r.is_ordered = True
            r.save()

        change_in_order.is_ordered=True
        change_in_order.save()                   
        context={
            'order' : change_in_order,
            }
        return render(request, 'cart/order_confirmed.html', context)
    except ObjectDoesNotExist:
        return HttpResponse('No items in Your cart, Either it just got ordered by someone else, Try for other products please!')


@login_required
def checkOut(request):
    if request.method == 'POST':
        updateForm = updateUserForm(request.POST, instance=request.user.profile)
        update_email = updateEmail(request.POST, instance=request.user)
        context = {'updateForm':updateForm,
        'update_email': update_email,}
        if updateForm.is_valid() and update_email.is_valid():
            updateForm.save()
            update_email.save()
            messages.info(request, "Address updated , Choose payment mode and click checkout")
            orders = Order.objects.get(user=request.user, is_ordered=False)
            context['order']=orders
            return redirect('cart:checkout')
        else:
            messages.info(request, "Some thing getting wrong ..")
    else:
        updateForm = updateUserForm(instance=request.user.profile)
        update_email = updateEmail( instance=request.user)
        try:
            orders = Order.objects.get(user=request.user, is_ordered=False)
            context = {'updateForm':updateForm,
            'update_email': update_email,
            'order':orders,
            }
            return render(request, 'cart/checkout.html', context)
        except ObjectDoesNotExist:
            return HttpResponse("No items in Your cart, Either it just got ordered by someone else, Try for other products please!")



@login_required
def checkout_to_payment(request):
    user_profile_detail = Profile.objects.get(user=request.user)
    order_to_save = Order.objects.get(user=request.user, is_ordered=False)
    order_to_save.total_price=order_to_save.get_cart_total()
    order_to_save.shipping_address = f"pyTM{user_profile_detail.name}> <{user_profile_detail.number}> <{request.user.email}> <{user_profile_detail.address}> <{user_profile_detail.landmark}> <{user_profile_detail.city}> <{user_profile_detail.pinCode}"
    order_to_save.ordered_date = datetime.now()
    order_to_save.save()
    parameter_dict_paytm = {

                    'MID': settings.PAYTM_MERCHANT_ID,
                    'ORDER_ID': str(order_to_save.ref_code),
                    'TXN_AMOUNT': str(order_to_save.get_cart_total()),
                    'CUST_ID': str(request.user.email),
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': 'WEBSTAGING',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL':'http://127.0.0.1:8000/cart/handle-request/',}
    parameter_dict_paytm['CHECKSUMHASH'] = checksum.generate_checksum(parameter_dict_paytm, settings.PAYTM_MERCHANT_KEY)
    return render(request, 'cart/paytm.html', {'parameter_dict_paytm':parameter_dict_paytm,})



@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    checksum_=''
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum_ = form[i]
    verify = checksum.verify_checksum(response_dict, settings.PAYTM_MERCHANT_KEY, checksum_)
    if verify:
        if response_dict['RESPCODE'] == '01':
            change_in_order = Order.objects.get(user=request.user, is_ordered=False)
            for r in change_in_order.get_cart_items():
                r.is_ordered = True
                r.save()

            change_in_order.is_ordered=True
            change_in_order.save()
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'cart/payment_status.html', {'response': response_dict})