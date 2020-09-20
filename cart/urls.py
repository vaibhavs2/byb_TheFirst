from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
  path('', views.order_summary, name='yo'),
  path('delete-item/<str:itemId>',views.delete_from_cart,  name = 'delete_item'),
  path('check-out/',views.checkOut, name='checkout'),
  path('order-confirm/',views.order_confirmed, name='order_confirm' ),
  path("handle-request/", views.handlerequest, name="HandleRequest"),
  path('checkout-to-payment/', views.checkout_to_payment, name='checkout_to_payment')
  
]