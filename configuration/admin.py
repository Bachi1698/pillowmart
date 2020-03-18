from django.contrib import admin
from . import models

# Register your models here.
class SocialCountAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update')
    liste_filter = ('status',)
    search_fields = ('nom',)
    date_hierachy = "date_add"
    ordering = ['nom']
    list_per_page = 6

class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('email','date_add','date_update','logo_view')
    liste_filter = ('status',)
    search_fields = ('email',)
    date_hierachy = "date_add"
    ordering = ['email']
    list_per_page = 6

    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))

class PresentationAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','image_view')
    liste_filter = ('status',)
    search_fields = ('nom',)
    date_hierachy = "date_add"
    ordering = ['nom']
    list_per_page = 6

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','date_add','date_update','image_view')
    liste_filter = ('status',)
    search_fields = ('nom',)
    date_hierachy = "date_add"
    ordering = ['nom']
    list_per_page = 6

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))







def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.SocialCount,SocialCountAdmin)
_register(models.SiteInfo,SiteInfoAdmin)
_register(models.Presentation,PresentationAdmin)
_register(models.Temoignage,TemoignageAdmin)

