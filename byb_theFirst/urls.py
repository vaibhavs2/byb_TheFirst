"""byb_TheFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sell import views as sell_views
from  django.conf.urls import include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('sriKrishna/', admin.site.urls),
    path('',include('theFirst.urls')),
    path('sell/',sell_views.sellIndex, name = 'sellform' ),
    path('product/',include('product.urls')),
    path('user/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'user/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'user/password_reset_complete.html'), name='password_reset_complete'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name = 'user/passwordChange.html'), name='ChangePassword'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'user/password_reset_complete.html'), name='password_change_done'),
]
