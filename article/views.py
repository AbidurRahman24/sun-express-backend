from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
# Create your views here.
def send_transaction_email(user, rating, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'rating' : rating,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class =  serializers.ArticleSerializer

class ReviewViewset(viewsets.ModelViewSet):
    # user = 
    queryset = models.Review.objects.all()
    # print("This",queryset)
    serializer_class = serializers.ReviewSerializer

    def list(self, request, *args, **kwargs):
        for review in self.get_queryset():
            viewer_email = review.viewer.user
            email_subject = "Review"
            email_body = render_to_string('review_email.html')
            email = EmailMultiAlternatives(email_subject , '', to=[viewer_email.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return super().list(request, *args, **kwargs)