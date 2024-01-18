from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # wifi toiri korlam
router.register('list', views.ArticleViewSet) # ekta entena toiri korlam
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    path('reviews/', views.ReviewCreateView.as_view(), name='create-review'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<int:id>', views.edit_article, name='edit_article'),
    path('delete/<int:id>', views.delete_article, name='delete_article'),
    path('', include(router.urls)),
    # path('articles/<int:article_id>/', SpecificArticleView.as_view(), name='specific_article'),
]