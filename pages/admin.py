from django.contrib import admin

from . import models

admin.site.register(models.BlogPost)
admin.site.register(models.Certificat)

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



admin.site.site_header  =  "Bosh sahifa"
admin.site.index_title  =  "Holmon Alp"
admin.site.site_title  =  "sayt Admin"
 