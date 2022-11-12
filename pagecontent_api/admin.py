from django.contrib import admin
from pagecontent_api.models import PressContent

@admin.register(PressContent)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['date']
    list_display = ['pk', 'label','url','date','created','modified']