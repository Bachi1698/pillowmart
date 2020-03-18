from django.contrib import admin
from . import models

# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','image_view')
    liste_filter = ('status',)
    search_fields = ('nom',)
    date_hierachy = "date_add"
    ordering = ['nom']
    list_per_page = 6

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom','prix','date_add','date_update','image_view')
    liste_filter = ('status',)
    search_fields = ('nom',)
    date_hierachy = "date_add"
    ordering = ['nom']
    list_per_page = 6

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Categorie,CategorieAdmin)
_register(models.Produit,ProduitAdmin)


