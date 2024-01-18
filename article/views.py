from django.shortcuts import render, redirect
from rest_framework import viewsets
from . import models
from . import serializers
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import generics
from . import forms
from . import models
# Create your views here.
# def send_transaction_email(user, rating, subject, template):
#         message = render_to_string(template, {
#             'user' : user,
#             'rating' : rating,
#         })
#         send_email = EmailMultiAlternatives(subject, '', to=[user.email])
#         send_email.attach_alternative(message, "text/html")
#         send_email.send()
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class =  serializers.ArticleSerializer
    filter_backends = [filters.SearchFilter]
    # print(filter_backends)
    # search_fields = ['headline', 'body', 'category__name', 'editor__user']
    search_fields = [ 'category__name', 'category__slug', 'ratings']
    

class articleForSpecific(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        article_id = request.query_params.get("article_id")
        if article_id:
            return query_set.filter(article_id = article_id)
        return query_set

# class ReviewCreateView(generics.CreateAPIView):
#     queryset = models.Review.objects.all()
#     serializer_class = serializers.ReviewSerializer

class ReviewViewset(viewsets.ModelViewSet):
    
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    # filter_backends = [filters.SearchFilter]
    filter_backends = [filters.SearchFilter,articleForSpecific]
    search_fields = ['rating']

    # def list(self, request, *args, **kwargs):
    #     for review in self.get_queryset():
    #         viewer_email = review.viewer.user
    #         email_subject = "Review"
    #         email_body = render_to_string('review_email.html')
    #         email = EmailMultiAlternatives(email_subject , '', to=[viewer_email.email])
    #         email.attach_alternative(email_body, "text/html")
    #         email.send()
    #         return Response("Check your mail for confirmation")
    #     return super().list(request, *args, **kwargs)
def add_article(request):
    if request.method == 'POST': # user post request koreche
        article_form = forms.AritcleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('add_article')
    
    else: # user normally website e gele blank form pabe
        article_form = forms.AritcleForm()
    return render(request, 'add_article.html', {'form' : article_form})


def edit_article(request, id):
    article = models.Article.objects.get(pk=id) 
    article_form = forms.AritcleForm(instance=article)
    # print(post.title)
    if request.method == 'POST':
        article = forms.AritcleForm(request.POST, instance=article) 
        if article_form.is_valid():
            article_form.save() 
            return redirect('homepage')
    
    return render(request, 'add_article.html', {'form' : article_form})

def delete_article(request, id):
    article = models.Article.objects.get(pk=id) 
    article.delete()
    return redirect('homepage')