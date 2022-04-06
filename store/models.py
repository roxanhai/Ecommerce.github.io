import random
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer',null=True, blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.name

    @property
    def get_cart_total_quantity(self):
        for temp_order in Order.objects.all().filter(customer=self):
            if temp_order.completed == False:
                return temp_order.get_cart_total_quantity
        return 0
    
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url 
        
         
    BOOK = "B"
    MOBILE_PHONE = "MP"
    CLOTHES = "C"
    LAPTOP = "L"
    SHOES = "S"
    ELECTRONIC = "E"
    CATEGORIES_CHOICE = [
        (BOOK,"Book"), (MOBILE_PHONE,"Mobile Phone"),(CLOTHES,"Clothes"),
        (LAPTOP,"Laptop"),(SHOES,"Shoes"),(ELECTRONIC,"Electronics")
    ]
    category = models.CharField(max_length=20,choices=CATEGORIES_CHOICE,default=BOOK)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200,null=True,unique=True,
                                      default=str(random.randint(10000,99999)))
    completed = models.BooleanField(default=False,null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False :
                shipping = True
        return shipping
    
    @property
    def get_cart_total_price(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_total_quantity(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def get_oder_items(self):
        return  self.orderitem_set.all()
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)    
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return self.address 
    