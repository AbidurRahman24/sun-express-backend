"""
URL configuration for sunExpress project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('category/<slug:category_slug>/', views.home, name='category_wise_post'),
    path('viewer/', include('viewer.urls')),
    path('editor/', include('editor.urls')),
    path('category/', include('category.urls')),
    path('article/', include('article.urls')),
    path('poll/', include('polls.urls')),
    # re_path(r'^.*$', TemplateView.as_view(template_name='404.html'), name='catch_all'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)