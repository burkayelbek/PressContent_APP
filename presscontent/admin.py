from django.contrib import admin
from presscontent.models import PressContent


@admin.register(PressContent)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['date']
    list_display = ['pk', 'label', 'slug', 'date', 'created', 'modified']