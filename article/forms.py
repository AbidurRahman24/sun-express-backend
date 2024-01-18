from django import forms
from .models import Article,Comment

class AritcleForm(forms.ModelForm):
    class Meta: 
        model = Article
        # fields = '__all__'
        exclude = ['editor']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body','rating']