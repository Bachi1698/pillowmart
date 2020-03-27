from django.contrib import admin
from . import models

# Register your models here.
class CustomAddmin(admin.ModelAdmin):
    actions = ('activate','desactivate')
    list_filter = ('status',)
    list_per_page = 6
    date_hierachy = "date_add"

    def activate(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selection a été effectué avec succes')
    activate.short_description = "permet d'activer le champs selectionner"

    def desactivate(self,request,queryset):  
        queryset.update(status=False)
        self.message_user(request,'la selection a été effectué avec succes')
    desactivate.short_description = "permet de desactiver le champs selectionner"

class SocialCountAdmin(CustomAddmin):
    list_display = ('nom','date_add','date_update')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info social",{"fields":["nom","lien","icone"]}),
                  ("standard",{"fields":["status"]})
    ]

class SiteInfoAdmin(CustomAddmin):
    list_display = ('email','date_add','date_update','map_url','logo_view')
    search_fields = ('email',)
    ordering = ['email']
    fieldsets = [
                 ("info site",{"fields":["email","map_url","logo"]}),
                 ("standard",{"fields":["status"]})
    ]

    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))

class PresentationAdmin(CustomAddmin):
    list_display = ('nom','date_add','date_update','image_view')
    search_fields = ('nom',)
    ordering = ['nom']
    fieldsets = [
                 ("info presentation",{"fields":["nom","description","image","video"]}),
                 ("standard",{"fields":["status"]})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class TemoignageAdmin(CustomAddmin):
    list_display = ('nom','prenom','date_add','date_update','image_view')
    search_fields = ('nom',)
    ordering = ['nom']
    fieldsets = [
                ("info temoignage",{"fields":["nom","prenom","message","photo"]}),
                ("standard",{"fields":["status"]})
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))







def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.SocialCount,SocialCountAdmin)
_register(models.SiteInfo,SiteInfoAdmin)
_register(models.Presentation,PresentationAdmin)
_register(models.Temoignage,TemoignageAdmin)

