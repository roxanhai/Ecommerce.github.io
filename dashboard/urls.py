from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('product_manage/',views.productManage,name="product_manage"),
    path('customer_manage/',views.customerManage,name="customer_manage")
]
