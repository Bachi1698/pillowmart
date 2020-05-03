from django.shortcuts import render, redirect
from . import forms 
from configuration import models as configuration_models
# Create your views here.


def inscription(request):
    form=""
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.RegistrationForm()
    
    datas = {
        'form':form,
        
    }
    return render(request, "registration/inscription.html", datas)

