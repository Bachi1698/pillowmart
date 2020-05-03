from django.shortcuts import render, redirect
from . import forms 
from configuration import models as configuration_models
# Create your views here.


def inscription(request):
    site_info = configuration_models.SiteInfo.objects.filter(status=True)[:1].get()
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
        'site_info':site_info,
        
    }
    return render(request, "registration/inscription.html", datas)

