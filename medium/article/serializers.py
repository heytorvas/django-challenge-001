from author.serializers import AuthorSerializer
from article.models import Article

from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id', 
            'category', 
            'title', 
            'summary', 
            'first_paragraph', 
            'body', 
            'author'
        ]

class ArticleSlugSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = [
            'id', 
            'author', 
            'category', 
            'title', 
            'summary'
        ]

class AnonymousArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = [
            'id', 
            'author', 
            'category', 
            'title', 
            'summary', 
            'first_paragraph'
        ]

class LoggedArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = "__all__"