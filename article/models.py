from django.db import models
from category.models import Category
from editor.models import Editor
from viewer.models import Viewer
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publishing_time = models.DateTimeField(auto_now_add=True)
    ratings = models.IntegerField(default=0)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)

    # Additional necessary fields
    image = models.ImageField(upload_to='article/images/', null=True, blank=True)

    def __str__(self):
        return self.headline
    

class Review(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete = models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')])
    
    def __str__(self):
        return f"Viewer : {self.viewer.user.first_name} ; Article {self.article.headline}"