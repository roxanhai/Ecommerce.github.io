from django.shortcuts import render
from store.models import *
# Create your views here.
def dashboard(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    print(customer)
    print(order)
    context = {
        "customerList": customer,
        "orderList": order,
    }
    return render(request,"dashboard/dashboard.html",context)

def productManage(request):
    context = {}
    return render(request,"dashboard/product.html",context)

def customerManage(request):
    context = {}
    return render(request,"dashboard/customer.html",context)