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
    category = models.ManyToManyField(Category)
    publishing_time = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    ratings = models.IntegerField(default=0)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article/images/', null=True, blank=True)


    def likes_count(self):
        return self.like_set.count()
    
    
    def save(self, *args, **kwargs):
        update_last_updated = kwargs.pop('update_last_updated', True)
        
        if update_last_updated or not self.pk: 
            self.last_updated = timezone.now()

        super().save(*args, **kwargs)
        
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
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name}"