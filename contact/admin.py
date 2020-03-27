from django.contrib import admin
from . import models

# Register your models here.
class CustomAdmin(admin.ModelAdmin):
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

class NewsletterAdmin(CustomAdmin):
    list_display = ('email','date_add','date_update')
    search_fields = ('nom',)
    list_display_links = ['email']
    fieldsets = [
                 ("info contact",{"fields":["email"]}),
                 ("standard",{"fields":["status"]})
    ]

class ContactAdmin(CustomAdmin):
    list_display = ('nom','email','date_add','date_update')
    search_fields = ('email',)
    ordering = ['email']
    fieldsets = [
                  ("info newsletter",{"fields":["email","nom","message","sujet"]}),
                  ("foreign keys",{"fields":["status"]})
    ]
    
def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Contact,ContactAdmin)
_register(models.Newsletter,NewsletterAdmin)



