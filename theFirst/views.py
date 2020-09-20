from django.shortcuts import render, get_object_or_404, redirect
from .models import GoodDeals, branch, order_deals
from django.urls import reverse
from product.models import bestSelling, Product
from django.views.generic import DetailView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import re
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from cart import checksum
from product.views import create_ref_code
# Create your views here.


single_book = GoodDeals.objects.filter(bookSets = False)
single_list_book_branch = []
for  r in single_book:
   single_list_book_branch.append( ''.join(re.findall(r'[A-Z]',str(r.branch))))

def index(request):
    context = {
        'book_set' : GoodDeals.objects.filter(bookSets = True),
        'single_book':zip(single_book, single_list_book_branch),
        'bestSelling': bestSelling.objects.all(),
        'branches':branch.objects.all(),    }
    return render(request,'theFirst/index.html',context) 


class ProductFilteredListView(ListView):
    model = Product
    template_name = 'product/product_view.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        id = get_object_or_404(branch, id=self.kwargs.get('branch_id'))
        return Product.objects.filter(branch_id=id).order_by('?')


def help_page(request):
    return render(request,'footers/help.html')

def career_page(request):
    return render(request,'footers/formCareer.html')

def privacy_page(request):
    return render(request,'footers/privacy.html')

def aboutUs_page(request):
     return render(request,'footers/about_Us.html')



def check_stocks(request):

    product_list = GoodDeals.objects.filter(InStock=0).values_list('id',flat=True)
    product_list = list(product_list)
    product_list = [str(i) for i in product_list]
    product_list=','.join(product_list)
    data={
        'filtered_stock_list': product_list,
            }

    return JsonResponse(data)


@login_required
def checkout_to_payment(request, itemId):
    user_profile_detail = Profile.objects.get(user=request.user)
    item = GoodDeals.objects.get(id=itemId)
    order_save, status=order_deals.objects.get_or_create(user=request.user, product=item, is_ordered=False)
    if status:
        order_save.adress = f"pyTM{user_profile_detail.name}> <{user_profile_detail.number}> <{request.user.email}> <{user_profile_detail.address}> <{user_profile_detail.landmark}> <{user_profile_detail.city}> <{user_profile_detail.pinCode}"
        order_save.ordered_date = datetime.now()
        order_save.ref_code = create_ref_code()
        order_save.save()
    else:
        messages.WARNING(request, "Error occured, don't worry we are fixing it. . ")
    parameter_dict_paytm = {

                    'MID': settings.PAYTM_MERCHANT_ID,
                    'ORDER_ID': str(order_save.ref_code),
                    'TXN_AMOUNT': str(order_save.product.priceTosell),
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
            change_in_order = order_deals.objects.get(user=request.user, is_ordered=False)
            change_in_order.product.stock -= 1
            change_in_order.product.save()
            change_in_order.is_ordered=True
            change_in_order.save()
            print('order successful')
        else:
            messages(request,"Payment not completed, try cash on delivery")
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'cart/payment_status.html', {'response': response_dict})




@login_required()
def order_confirmed(request, itemId):
    user_profile_detail = Profile.objects.get(user=request.user)
    item = GoodDeals.objects.get(id=itemId)
    order_save, status=order_deals.objects.get_or_create(user=request.user, product=item, is_ordered=False)
    if status:
        order_save.adress = f"pyTM{user_profile_detail.name}> <{user_profile_detail.number}> <{request.user.email}> <{user_profile_detail.address}> <{user_profile_detail.landmark}> <{user_profile_detail.city}> <{user_profile_detail.pinCode}"
        order_save.ordered_date = datetime.now()
        order_save.ref_code = create_ref_code()
        order_save.save()
        if item.InStock >0:
            item.InStock -= 1
            item.save()
            order_save.is_ordered = True
            order_save.save()
        else:
            return HttpResponse('it just got ordered by someone else, Try for other products please!')
    else:
        messages.info(request, "Error occured, don't worry we are fixing it. . ")
                  
        context={
            'order' : order_save,
            }
        return render(request, 'cart/order_confirmed.html', context)
        