from django.contrib import admin
from urlcutsite.models import Url
 
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id','url','created_at', 'counter', 'submitter')
    ordering = ('-created_at',)
 
admin.site.register(Url, UrlsAdmin)
