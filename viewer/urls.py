from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('', views.ViewerViewset) 
urlpatterns = [
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='user_logout'),
    # path('profile/', views.profile, name='profile'),
    path('user/<int:user_id>/', views.UserDetailView.as_view(), name='user-detail'),
    # path('user/', views.UserProfileViewSet.as_view({'get': 'list'}), name='profile'),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    # path('req/', views.UserReg.as_view(), name='reg'),
    path('', include(router.urls)),
]