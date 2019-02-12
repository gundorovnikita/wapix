from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list_url'),
    path('list/<str:slug>', product_detail, name='product_detail_url'),
    path('add_to_cart/<str:slug>', add_to_cart_view, name='add_to_cart_url'),
    path('cat/<str:slug>', category_detail, name='category_detail_url'),
    path('cart/', cart_view, name='cart_view_url'), 
    path('mark/<str:slug>', mark_detail, name='mark_detail_url'),
]
