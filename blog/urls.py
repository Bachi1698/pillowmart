from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('about', views.about, name='about'),
     path('blog', views.blog, name='blog'),
      path('product_list', views.product_list, name='product_list'),
     path('single_blog', views.single_blog, name='single-blog'),
     path('single_product/<int:pk>', views.single_product, name='single-product'),
    
]