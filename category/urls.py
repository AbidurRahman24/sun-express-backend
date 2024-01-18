from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.CategoryViewset) # router er antena

urlpatterns = [
    path('add/', views.add_category, name='add_category'),
    path('', include(router.urls)),
]