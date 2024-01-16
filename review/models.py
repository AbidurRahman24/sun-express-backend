# from django.db import models
# from article.models import Article
# from viewer.models import Viewer
# # Create your models here.
# STAR_CHOICES = [
#     ('⭐', '⭐'),
#     ('⭐⭐', '⭐⭐'),
#     ('⭐⭐⭐', '⭐⭐⭐'),
#     ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
#     ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
# ]
# class Review(models.Model):
#     viewer = models.ForeignKey(Viewer, on_delete = models.CASCADE)
#     article = models.ForeignKey(Article, on_delete = models.CASCADE)
#     created = models.DateTimeField(auto_now_add = True)
#     rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
#     def __str__(self):
#         return f"Viewer : {self.viewer.user.first_name} ; Article {self.article.headline}"