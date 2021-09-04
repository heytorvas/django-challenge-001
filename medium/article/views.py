from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING

from django.shortcuts import render

from rest_framework import permissions, viewsets, views, status
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework_simplejwt.authentication import JWTAuthentication

from article.models import Article
from article.serializers import AnonymousArticleSerializer, ArticleSerializer, ArticleSlugSerializer, LoggedArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """This endpoint allows post, get, put, patch and delete of article from database"""

    authentication_classes = [JWTAuthentication]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    

class ArticleByCategory(views.APIView):
    """This endpoint list all articles filtered by category from the database"""
    permission_classes = [permissions.AllowAny]
    serializer_class = ArticleSlugSerializer

    @swagger_auto_schema(
        manual_parameters=[
            Parameter('category', IN_QUERY, type=TYPE_STRING, required=True),
        ],
        tags=['special']
    )
    def get(self, request, format=None):
        query_string = str(request.GET.get('category', ""))
        articles = Article.objects.filter(category__exact=query_string)
        serializer = ArticleSlugSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetByIdArticles(views.APIView):
    """This endpoint returns specific article filtered by id from the database"""
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(tags=['special'])
    @action(detail=False, methods=['get'])
    def get(self, request, id,  format=None):
        article = Article.objects.filter(id__exact=id)
        if request.user.is_anonymous:
            serializer = AnonymousArticleSerializer(article, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.user.is_authenticated:
            serializer = LoggedArticleSerializer(article, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
