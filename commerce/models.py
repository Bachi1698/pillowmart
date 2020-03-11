from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField('images/Categorie')
    description = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField("images/Produit")
    prix = models.FloatField()
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='article_categorie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)




