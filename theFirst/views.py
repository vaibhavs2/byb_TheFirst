from django.shortcuts import render, get_object_or_404
from .models import GoodDeals, branch
from product.models import bestSelling, Product
from django.views.generic import DetailView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
import re
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

@login_required
def cart_page(request):
    return render(request, 'footers/cart.html')