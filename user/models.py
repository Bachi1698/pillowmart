from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profil(models.Model):
    adresse = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to="images/user", default="image/article/pexels-photo-1082958.jpeg")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User_profil')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profil.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
            
        instance.User_profil.save()
