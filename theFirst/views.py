from django.shortcuts import render
from .models import GoodDeals, bestSelling, branch
# Create your views here.


def index(request):
    context = {
        'gooddeals' : GoodDeals.objects.all(),
        'bestSelling': bestSelling.objects.all(),
        'branches':branch.objects.all(),    }
    return render(request,'theFirst/index.html',context) 

