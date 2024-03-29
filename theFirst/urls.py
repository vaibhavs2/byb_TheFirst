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

from django.urls import path
from theFirst import views
from django.conf.urls import url
from product.views import ProductDetailView
from .views import ProductFilteredListView
app_name = 'theFirst'
urlpatterns = [
    path('', views.index, name='index'),
    path('help/',views.help_page, name='help'),
    path('careers/',views.career_page, name='career'),
    path('privacy/',views.privacy_page, name ='privacy'),
    path('about_us/', views.aboutUs_page,name='aboutUs'),
    path('product/detail/<str:pk>', ProductDetailView.as_view(), name='productDetail'),
    path('product/branch/<str:branch_id>',ProductFilteredListView.as_view(),name='filterd'),
]
