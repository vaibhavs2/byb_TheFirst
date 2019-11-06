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
app_name = 'product'
from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('detail/<str:pk>', views.ProductDetailView.as_view(), name='productDetail'),
    path('add-to-cart/', views.add_to_cart, name='add_To_cart'),
    path('search-items/',views.searchItems, name='search_result'),
    path('filter-product-stock/', views.check_stocks, name='filter_product_stock'),
       # path('detail/' ,views.product_detail ,name='productDetail'),
]
