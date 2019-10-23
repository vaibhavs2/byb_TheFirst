from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from users.models import Profile
from django.contrib.auth.password_validation import CommonPasswordValidator



class UserRegistrationForm (UserCreationForm):
    email = forms.EmailField()
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)] )

    class Meta:
        model = User
        fields = ['username','email','password1', ]        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Must be Unique'
        self.fields.pop('password2')


class updateUserForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['name', 'number', 'address','landmark', 'pinCode','city', ]

