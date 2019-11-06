from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from sell.sellForms import sellform
from sell.models import sell_order
from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def sellIndex(request):
    if request.method == 'POST':
        sellForm = sellform(request.POST)
        context = {'sellForm':sellForm,}
        if sellForm.is_valid(): 
            t=sellForm.save(commit=False)
            t.selling_user=request.user
            t.save()
            messages.success(request, f'SUCCESS! Your Oder has been placed, Our delivery executive will reach you within 3 days')
            return redirect('profile')
    else:
        
        sellForm = sellform()
        context = {'sellForm':sellForm}
    return render(request, 'sell/sellform.html', context)