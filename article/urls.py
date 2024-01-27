from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # wifi toiri korlam
router.register('list', views.ArticleViewSet) # ekta entena toiri korlam
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    # path('reviews/', views.ReviewViewset.as_view(), name='create-review'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<int:id>', views.edit_article, name='edit_article'),
    path('delete/<int:id>', views.delete_article, name='delete_article'),
    path('details/<int:id>/', views.DetailArticleView.as_view(), name='detail_article'),
    path('post/<int:id>/', views.like_post, name='like_post'),
    path('', include(router.urls)),
]