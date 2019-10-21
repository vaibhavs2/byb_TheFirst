from django.shortcuts import render
from .models import GoodDeals, bestSelling, branch
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {
        'gooddeals' : GoodDeals.objects.all(),
        'bestSelling': bestSelling.objects.all(),
        'branches':branch.objects.all(),    }
    return render(request,'theFirst/index.html',context) 

def help_page(request):
    return render(request,'footers/help.html')

def career_page(request):
    return render(request,'footers/formCareer.html')
def privacy_page(request):
    return render(request,'footers/privacy.html')
def aboutUs_page(request):
     return render(request,'footers/about_Us.html')

@login_required
def cart_page(request):
    return render(request, 'footers/cart.html')