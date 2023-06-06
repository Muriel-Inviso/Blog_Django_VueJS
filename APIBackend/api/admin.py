from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Article)
class ArticleModel(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title',)
    

