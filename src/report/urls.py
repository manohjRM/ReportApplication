from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('add_customer',add_customer,name='add_customer'),
    url(r'^edit_customer/(?P<pk>\d+)$',edit_customer, name='edit_customer'),
    url(r'^del_customer/(?P<pk>\d+)$',del_customer, name='del_customer'),
]