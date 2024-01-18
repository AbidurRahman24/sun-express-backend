from django.db import models
from category.models import Category
from editor.models import Editor
from viewer.models import Viewer
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publishing_time = models.DateTimeField(auto_now_add=True)
    ratings = models.IntegerField(default=0)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article/images/', null=True, blank=True)

    def __str__(self):
        return self.headline
    

class Review(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete = models.CASCADE, default=1)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')])
    
    def __str__(self):
        return f"Viewer : {self.viewer.user.first_name} ; Article {self.article.headline}"

class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    rating = models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')])
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
# class UserReview(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
#     rating = models.IntegerField(choices=[(i, i) for i in range(5)])
#     comment = models.TextField(default='')

#     def __str__(self):
#         return f"{self.user.username}'s review on {self.article.headline}"