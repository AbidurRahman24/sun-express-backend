from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class EditorViewset(viewsets.ModelViewSet):
    queryset = models.Editor.objects.all()
    serializer_class = serializers.EditorSerializer