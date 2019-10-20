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
urlpatterns = [
    path('shriKrishna/', admin.site.urls),
    path('',include('theFirst.urls')),
    path('sell/',sell_views.sellIndex, name = 'sellform' ),
    path('product/',include('product.urls')),
    path('user/', include('users.urls')),
]
