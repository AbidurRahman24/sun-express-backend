from django.shortcuts import render
from article.models import Article

def home(request):
    data = Article.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    #     print()
    return render(request, 'home.html', {'data' : data})