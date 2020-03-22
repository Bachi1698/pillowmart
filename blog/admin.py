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
    fieldsets = [
                  ("info tag",{"fields":["nom","description",]}),
                  ("standard",{"fields":["status"]})
    ]
class ArticleInline(admin.StackedInline):
    model = models.Article
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','date_add','date_update','status','image_view')
    list_filter = ('status',)
    search_fields = ('titre',)
    date_hierarchy = "date_add"
    list_per_page = 6
    ordering = ['titre']
    filter_horizontal = ["tag"]
    fieldsets = [
                    ("info article",{"fields":["titre","description","contenu","image"]}),
                    ("foreign keys",{"fields":["categorie","tag"]}),
                    ("standard",{"fields":["status"]})
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
    fieldsets = [
                ("info commentaire",{"fields":["nom","prenom","commentaire"]}),
                ("foreignkeys info",{"fields":["article"]}),
                ("standard",{"fields":["status"]}) 
     ]

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
    
    def activate(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selection a été effectué avec succes')
    activate.short_description = "permet d'activer les categories selectionner"

    def desactivate(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selection a été effectué avec succes')
    desactivate.short_description = "permet de desactiver les categories selectionner"










def _register(model,admin_class):
    admin.site.register(model,admin_class)


_register(models.CategorieArticle, CategorieArticleAdmin)
_register(models.Tag,TagAdmin)
_register(models.Article,ArticleAdmin)
_register(models.Commentaire,CommentaireAdmin)






