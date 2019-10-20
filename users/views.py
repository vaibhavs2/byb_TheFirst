from django.shortcuts import render , redirect
from django.contrib import messages
from users.registerForm import UserRegistrationForm, updateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username').split()
            messages.success(request, f'Account Created for {username[0]}! Please LogIn with your credential')
            return redirect('index')
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
            return redirect('profile')
    else:
        updateForm = updateUserForm(instance=request.user.profile)
        context = {'updateForm':updateForm,}
    return render(request, 'user/profile.html', context)


def terms_condition(request):
    return render(request, 'footers/privacy.html')