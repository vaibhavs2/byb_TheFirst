app_name = 'cart'
from django.urls import path
from cart import views

urlpatterns = [
  path('', views.order_summary, name='yo'),
  path('delete-item/<str:itemId>',views.delete_from_cart,  name = 'delete_item'),
  
]