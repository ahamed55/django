from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('order_form',views.order_form,name='order_form'),
    path('update_form/<str:pk>/',views.update_form,name='update_form'),
    path('delete_order/<str:pk>/',views.delete_order,name='delete_order'),
]