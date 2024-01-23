from article.models import Article, Comment
from category.models import Category
from django.shortcuts import render, redirect
from . import forms
from rest_framework import viewsets, filters
from . import models
from . import serializers
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

# Create your views here.

def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save() 
            return redirect('add_category')
    
    else: 
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form' : category_form})

def category(request, category_slug = None):
    # print(category_slug)
    data = Article.objects.all() 
    if category_slug is not None: #
        category = Category.objects.get(slug = category_slug) 
        data = Article.objects.filter(category  = category) 
    categories = Category.objects.all()
    category_slug = category_slug
    return render(request, 'categoryPage.html', {'data' : data, 'category' : categories, 'category_slug':category_slug})
