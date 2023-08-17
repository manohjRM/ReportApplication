from django.urls import path, re_path
# from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('add_customer',add_customer,name='add_customer'),
    re_path(r'^edit_customer/(?P<pk>\d+)$',edit_customer, name='edit_customer'),
    re_path(r'^del_customer/(?P<pk>\d+)$',del_customer, name='del_customer'),
]