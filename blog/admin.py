from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status',)
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hieararchy = "date_add"
    ordering = ['nom']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','date_add','date_update','status','image_view')
    list_filter = ('status',)
    search_fields = ('titre',)
    date_hierarchy = "date_add"
    list_per_page = 6
    ordering = ['titre']
    fieldsets = [
                    ("info article",{"fields":["titre","description","contenu","image"]})
                    # ("standard",{"fields":["status"]})
    ]
    def image_view(self,obj):
        return mark_safe("<img src'{url}' width='100px',height='50px'>".format(url=obj.iamge.url))

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','date_add','date_update','image_view')
    liste_filter = ('status',)
    search_fields = ('nom',)
    date_hierachy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 6

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


class CategorieArticleAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status','image_view')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 6
    fieldsets = [
                    ("info categorie",{"fields":["nom","image","description"]}),
                    ("standard",{"fields":["status"]})
                ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))









def _register(model,admin_class):
    admin.site.register(model,admin_class)


_register(models.CategorieArticle, CategorieArticleAdmin)
_register(models.Tag,TagAdmin)
_register(models.Article,ArticleAdmin)
_register(models.Commentaire,CommentaireAdmin)






