from django.shortcuts import render
from . import models
from commerce import models as commerce_models
from configuration import models as configuration_models

# Create your views here.
def index(request):
    article = models.Article.objects.filter(status=True)[:3]
    produit = commerce_models.Produit.objects.filter(status=True)
    site_info = configuration_models.SiteInfo.objects.filter(status=True)[:1].get()
    datas = {
            'article':article ,
            'produit' : produit,
            'site_info':site_info,
    }
    return render(request,'pages/index.html',datas)
def about(request):
    presentation = configuration_models.Presentation.objects.filter(status=True)
    datas = {
                'presentation': presentation,
    }
    return render(request,'pages/about.html',datas)
def blog(request):
    datas = {

    }
    return render(request,'pages/blog.html',datas)
def product_list(request):
    datas = {

    }
    return render(request,'pages/product_list.html',datas)
def single_blog(request):
    datas = {

    }
    return render(request,'pages/single-blog.html',datas)
def single_product(request):
    datas = {

    }
    return render(request,'pages/single-product.html',datas)