from ctypes import addressof
from email.headerregistry import Address
import json
import json.decoder
from sre_parse import State
from types import CoroutineType
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import datetime
#Page
# @login_required(login_url = 'login')
def store(request):
    pList = Product.objects.all()
    context = {
        "productList": pList
    }
    return render(request,'store/store.html',context)

@login_required(login_url = 'login')
def cart(request):
    if request.user.is_authenticated: #If User Login
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        itemList = order.orderitem_set.all()
    else: #If User not Login
        itemList= []
        order = {"get_cart_total_price":0, "get_cart_total_quantity":0}
    context = {
        "order":order,
        "itemList":itemList,
    }
    return render(request,'store/cart.html',context)

@login_required(login_url = 'login')
def checkout(request):
    if request.user.is_authenticated: #If User Login
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        itemList = order.orderitem_set.all()
        context = {
        "user": customer,
        "order":order,
        "itemList":itemList,
    }
    else: #If User not Login
        itemList= []
        order = {"get_cart_total_price":0, "get_cart_total_quantity":0}
        context = {"itemList":itemList,}
   
    return render(request,'store/checkout.html',context)


#Account
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('store')
    else: 
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            # print(username)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                Customer.objects.create(name=username, email=email, user=user)
                messages.success(request,'Account was create for: ' + username)
                return redirect('login')
        
        context={'form':form}
        return render(request,'store/register.html',context)
    

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('store')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect('store')
            else:
                messages.info(request, 'Username OR Password is in corrrect')
        context={}
        return render(request,'store/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('store')

#Function Button (With JavaScript)
@login_required(login_url = 'login')
def addToCart(request): 
    #Request.body trả về dưới dạng byte 
    if request.user.is_authenticated:
        responseJson = request.body.decode('utf-8')
        data = json.loads(responseJson)
        productId = data['productId']
        action = data['actions']
        
        print('Action: ',action)
        print('Product: ', productId)
        
        customer = request.user.customer
        product = Product.objects.get(id = productId)
        order , created = Order.objects.get_or_create(customer=customer,completed=False)
        
        order_item, created = OrderItem.objects.get_or_create(order=order,product=product)
        
        if action=='add':
            order_item.quantity +=1
        elif action=='remove':
            order_item.quantity -=1
        
        order_item.save()
        if(order_item.quantity<=0):
            order_item.delete()
    return JsonResponse('Item was added to cart', safe=False)

def paymentOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        responseJson = request.body.decode('utf-8')
        data = json.loads(responseJson)
        
        userFormData = data['userFormData']
        userFormDataTotal = float(userFormData['total'])
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        order.transaction_id = transaction_id
        #Check lại phòng trường hợp Customer thay đổi giá trị total price trog JavaScript
        if userFormDataTotal == order.get_cart_total_price:
            order.completed = True
            print(userFormDataTotal) 
            print(order.get_cart_total_price)
            print(order.id)
            order.save()
        
        
        shippingFormData = data['shippingFormData']
        if(order.shipping==True):
            ShippingAddress.objects.create(
                customer = customer, 
                order = order,
                address = shippingFormData['address'],
                city = shippingFormData['city'],
                state = shippingFormData['state'], 
                zipcode = shippingFormData['zipcode'],
            )
        print('userFormData:',userFormData)
        print('shippingFormData:',shippingFormData)
    else:
        print("User is not logged in")
    return JsonResponse('Payment subbmitted..',safe=False)


#Admin-Staff

    
    

    