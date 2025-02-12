"""medium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import include

from rest_framework import routers
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_simplejwt import views

from author.views import AuthorViewSet
from article.views import ArticleViewSet, ArticleByCategory, GetByIdArticles

router = routers.DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"articles", ArticleViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="API Docs",
        default_version="v1",
        description="API Documentation for Django Challenge",
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/admin/', include(router.urls)),

    path('login/', views.TokenObtainPairView.as_view(), name='login'),
    path('signup/', include('auth.urls')),

    path("api/articles/", ArticleByCategory.as_view()),
    path("api/articles/<uuid:id>/", GetByIdArticles.as_view()),

    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0))
]
