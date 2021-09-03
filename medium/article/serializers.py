from author.serializers import AuthorSerializer
from author.models import Author
from rest_framework import serializers
from article.models import Article
from author.models import Author


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
