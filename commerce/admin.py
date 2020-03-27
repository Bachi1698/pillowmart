from django.contrib import admin
from . import models

# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    liste_filter = ('status',)
    date_hierachy = "date_add"
    list_per_page = 6
    actions =('activate','desactivate') 

    def activate(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selection a été effectué avec succes')
    activate.short_description = "permet d'activer le champs selectionner"

    def desactivate(self,request,queryset):  
        queryset.update(status=False)
        self.message_user(request,'la selection a été effectué avec succes')
    desactivate.short_description = "permet de desactiver le champs selectionner"
        
class CategorieAdmin(CustomAdmin):
    list_display = ('nom','date_add','date_update','image_view')    
    search_fields = ('nom',)    
    ordering = ['nom']
    
    fieldsets = [
                  ("info categorie",{"fields":["nom","description","image"]}),
                  ("standard",{"fields":["status"]})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class ProduitAdmin(CustomAdmin):
    list_display = ('nom','prix','date_add','date_update','image_view')
    search_fields = ('nom',)
    ordering = ['nom']
    fieldsets = [
                  ("info produit",{"fields":["nom","prix","image"]}),
                  ("foreignkeys",{"fields":["categorie"]}),
                  ("standard",{"fields":["status"]})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Categorie,CategorieAdmin)
_register(models.Produit,ProduitAdmin)


