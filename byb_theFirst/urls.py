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
from theFirst import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from sell import views as sell_views
from product.views import product_view
from  django.conf.urls import url, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'theFirst/',include('theFirst.urls')),
    path('signUp/', user_views.register,name='register'),
    path('logIn/', auth_views.LoginView.as_view(template_name = 'user/login.html'),name='login'),
    path('logOut/', auth_views.LogoutView.as_view(template_name = 'user/logout.html') ,name='logout'),
    path('profile/', user_views.profile, name = 'profile'),
    path('sell/',sell_views.sellIndex, name = 'sellform' ),
    path('product/',product_view, name="products"),
]
