from django.urls import path
from . import views

urlpatterns = [
     
     path('cart', views.cart, name='cart'),
     path('checkout', views.checkout, name='checkout'),
     path('confirmation', views.confirmation, name='confirmation'),
     path('contact', views.contact, name='contact'),
     path('elements', views.elements, name='elements'),
     path('login', views.login, name='login'),
    
]