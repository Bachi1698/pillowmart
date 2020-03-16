from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

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





