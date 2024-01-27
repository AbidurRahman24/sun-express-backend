
from django.shortcuts import render
from article.models import Article
from category.models import Category

def home(request, category_slug = None):
    data = Article.objects.all().order_by('-publishing_time')[:1]
    TotalData = Article.objects.all().order_by('?')[:4]
    if category_slug is not None: #
        category = Category.objects.get(slug = category_slug) 
        data = Article.objects.filter(category  = category) 
    sports_category = Category.objects.get(name='Sports')
    tech_category = Category.objects.get(name='Tech')
    sports_posts = Article.objects.filter(category=sports_category).order_by('-publishing_time')[:4]
    tech_posts = Article.objects.filter(category=tech_category).order_by('-publishing_time')[:2]
    random_data = Article.objects.all().order_by('?')[:7]
    categories = Category.objects.all()
    category = Category.objects.all().order_by('?')[:5]
    return render(request, 'home.html', {'category':category,'tech_posts':tech_posts,'sports_posts': sports_posts,'TotalData':TotalData,'data' : data, 'categories' : categories,'random_data':random_data})

