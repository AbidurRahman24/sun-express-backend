from django.contrib import admin
from . import models
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline','body', 'category','editor_name','publishing_time']
    def editor_name(self,obj):
        return obj.editor.user.first_name
class ReviewAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug' : ('name',)}
    list_display = ['article_headline','reviewer_name','rating', 'created']

    def article_headline(self,obj):
        return obj.article.headline
    def reviewer_name(self,obj):
        return obj.viewer.user.first_name

    
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Review, ReviewAdmin)
