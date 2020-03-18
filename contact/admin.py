from django.contrib import admin
from . import models

# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_add','date_update')
    liste_filter = ('status',)
    search_fields = ('nom',)
    date_hierachy = "date_add"
    list_display_links = ['email']
    list_per_page = 6

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom','email','date_add','date_update')
    liste_filter = ('status',)
    search_fields = ('email',)
    date_hierachy = "date_add"
    ordering = ['email']
    list_per_page = 6



def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Contact,ContactAdmin)
_register(models.Newsletter,NewsletterAdmin)



