from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters
# Create your views here.
class ArticleForSpecificCategory(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        article_id = request.query_params.get("article_id")
        if article_id:
            return query_set.filter(article_id = article_id)
        return query_set
class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [ArticleForSpecificCategory]