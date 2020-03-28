from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    actions = ('activate','desactivate')
    date_hierarchy = "date_add"
    list_per_page = 6
    search_fields = ('nom',)
    def activate(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selection a été effectué avec succes')
    activate.short_description = "permet d'activer le champs selectionner"

    def desactivate(self,request,queryset):  
        queryset.update(status=False)
        self.message_user(request,'la selection a été effectué avec succes')
    desactivate.short_description = "permet de desactiver le champs selectionner"

class TagAdmin(CustomAdmin):
    list_display = ('nom','date_add','date_update','status',)
    search_fields = ('nom',)
    ordering = ['nom']
    fieldsets = [
                  ("info tag",{"fields":["nom","description",]}),
                  ("standard",{"fields":["status"]})
    ]
class ArticleInline(admin.StackedInline):
    model = models.Article
    extra = 0

class ArticleAdmin(CustomAdmin):
    list_display = ('titre','date_add','date_update','status','image_view')
    search_fields = ('titre',)   
    ordering = ['titre']
    filter_horizontal = ["tag"]
    
    fieldsets = [
                    ("info article",{"fields":["titre","description","contenu","image"]}),
                    ("foreign keys",{"fields":["categorie","tag"]}),
                    ("standard",{"fields":["status"]})
    ]
    def image_view(self,obj):
        return mark_safe("<img src'{url}' width='100px',height='50px'>".format(url=obj.image.url))

   

class CommentaireAdmin(CustomAdmin):
    list_display = ('nom','prenom','date_add','date_update','image_view')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info commentaire",{"fields":["nom","prenom","commentaire"]}),
                ("foreignkeys info",{"fields":["article"]}),
                ("standard",{"fields":["status"]}) 
     ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


class CategorieArticleAdmin(CustomAdmin):
    list_display = ('nom','date_add','date_update','status','image_view')
    list_display_links = ['nom']
    ordering = ['nom']
    readonly_fields = ['image_view']
    actions = ('activate','desactivate')
    fieldsets = [
                    ("info categorie",{"fields":["nom","image","description"]}),
                    ("standard",{"fields":["status"]})
                ]
    inlines = [
                ArticleInline,
    ]
    

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))










def _register(model,admin_class):
    admin.site.register(model,admin_class)


_register(models.CategorieArticle, CategorieArticleAdmin)
_register(models.Tag,TagAdmin)
_register(models.Article,ArticleAdmin)
_register(models.Commentaire,CommentaireAdmin)






