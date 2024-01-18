
from django.shortcuts import render
from article.models import Article
from category.models import Category
def home(request, category_slug = None):
    
    data = Article.objects.all() 
    if category_slug is not None: #
        category = Category.objects.get(slug = category_slug) 
        data = Article.objects.filter(category  = category) 
    categories = Category.objects.all()
    return render(request, 'home.html', {'data' : data, 'category' : categories})


# from django.shortcuts import render
# from article.models import Article

# def home(request):
#     data = Article.objects.all()
#     # print(data)
#     # for i in data:
#     #     print(i.title)
#     #     for j in i.category.all():
#     #         print(j)
#     #     print()
#     return render(request, 'home.html', {'data' : data})
