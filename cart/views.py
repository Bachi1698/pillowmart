from django.shortcuts import render

# Create your views here.

def cart(request):
    datas = {

    }
    return render(request,'pages/cart.html',datas)
def checkout(request):
    datas = {

    }
    return render(request,'pages/checkout.html',datas)
def confirmation(request):
    datas = {

    }
    return render(request,'pages/confirmation.html',datas)
def contact(request):
    datas = {

    }
    return render(request,'pages/contact.html',datas)
def elements(request):
    datas = {

    }
    return render(request,'pages/elements.html',datas)
def login(request):
    datas = {

    }
    return render(request,'pages/login.html',datas)


