from django.db import models

# Create your models here.
class CategorieArticle(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Categorie')
    description = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.nom 

class Article(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    contenu = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/Article')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag,related_name='tag_article')
    categorie = models.ForeignKey(CategorieArticle,on_delete=models.CASCADE,related_name='produit_categorie')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.titre 

class Commentaire(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='article_commentaire')
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    commentaire = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'commentaire'
        verbose_name_plural = 'commentaires'

    def __str__(self):
        return self.commentaire 




