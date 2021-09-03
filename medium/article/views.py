from author.serializers import AuthorSerializer
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import action


from rest_framework import viewsets

from rest_framework_simplejwt.authentication import JWTAuthentication

from article.models import Article
from article.serializers import ArticleSerializer

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
