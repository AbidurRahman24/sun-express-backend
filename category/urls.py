from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.CategoryViewset) # router er antena

urlpatterns = [
    path('', views.category, name='category'),
    path('category/<slug:category_slug>/', views.category, name='category_wise_post'),
    path('add/', views.add_category, name='add_category'),
    path('', include(router.urls)),
]