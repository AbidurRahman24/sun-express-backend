from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # wifi toiri korlam
router.register('list', views.ArticleViewSet) # ekta entena toiri korlam
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
    # path('articles/<int:article_id>/', SpecificArticleView.as_view(), name='specific_article'),
]