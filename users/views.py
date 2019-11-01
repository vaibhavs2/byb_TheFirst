from django.shortcuts import render , redirect
from django.contrib import messages
from .models import UserOrders
from django.http import JsonResponse
from django.contrib.auth.models import User
from product.models import Product
from users.registerForm import UserRegistrationForm, updateUserForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm    
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username').split()
            messages.success(request, f'Account Created for {username[0]}! Please LogIn with your credential')
            return redirect('theFirst:index')
    else:
        form = UserRegistrationForm()
    return render (request, 'user/register.html',{'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        updateForm = updateUserForm(request.POST, instance=request.user.profile)
        context = {'updateForm':updateForm,}
        if updateForm.is_valid(): 
            updateForm.save()
            messages.success(request, f'Your crediantial has been Updated')
            return redirect('users:profile')
    else:
        updateForm = updateUserForm(instance=request.user.profile)
        orders = UserOrders.objects.filter(user__id=request.user.id).order_by('-order_Date')
        id_list = []
        try:
            for r in orders:
                id_list.append(int(r.product_id))
            user_product = Product.objects.filter(id__in = id_list)
        except TypeError:
            user_product=[]
        order_to_show = zip(orders, user_product)
        context = {'updateForm':updateForm,
                    'orders':order_to_show,
                    'check_if_ordered':user_product,
                    }
    return render(request, 'user/profile.html', context)


def terms_condition(request):
    return render(request, 'footers/privacy.html')

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists(),
    }
    return JsonResponse(data)