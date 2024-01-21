from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

# router.register('list', views.EditorViewset) # router er antena

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
     path('profile/edit', views.edit_profile, name='edit_profile'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    path('', include(router.urls)),
]