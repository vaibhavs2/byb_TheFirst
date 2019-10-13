from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name','number','city','address','landmark','pinCode')

admin.site.register(Profile, ProfileAdmin)
