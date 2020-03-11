from django.db import models

# Create your models here.

class Contact(models.Model):
    message = models.TextField(max_length=255)
    nom = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    sujet = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.nom

class Newsletter(models.Model):
    email = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'
    
    def __str__(self):
        return self.email

