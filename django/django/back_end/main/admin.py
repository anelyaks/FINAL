from django.contrib import admin
from .models import Articles
# Product, Category,


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']

