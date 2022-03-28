from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutUser,name="logout"),
    path('add_to_cart/',views.addToCart,name="add_to_cart"),
    path('payment_order/',views.paymentOrder,name="payment_order")
]
