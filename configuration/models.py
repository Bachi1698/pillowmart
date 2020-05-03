from django.db import models

# Create your models here.

class SocialCount(models.Model):
    ICONES = [
        ('facebook','fa-facebook-f'),
        ('instagram','fa-instagram'),
        ('google-plus','fa-google-plus-g'),
        ('linkedin','fa-linkedin-in'),
        
    ] 
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icone = models.CharField(choices=ICONES,max_length=20)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta: 
        verbose_name = 'social account'
        verbose_name_plural = 'socials account'
    
    def __str__(self):
        return self.nom

class SiteInfo(models.Model):
    logo = models.ImageField()
    email = models.CharField(max_length=255)
    map_url = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'site info'
        verbose_name_plural = 'sites infos'

    def __str__(self):
        return self.email

class Presentation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField('images/Presentation')
    video = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'presentation'
        verbose_name_plural = 'presentations'

    def __str__(self):
        return self.nom
    
class Temoignage(models.Model):
    photo = models.ImageField('images/Temoignage')
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'temoignage'
        verbose_name_plural = 'temoignages'

    def __str__(self):
        return self.nom



    
    
    
