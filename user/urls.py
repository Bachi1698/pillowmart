from django.urls import path, include
from.import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('', views.inscription, name='inscription'),

]
