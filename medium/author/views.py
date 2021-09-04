from django.shortcuts import render

from rest_framework import viewsets

from rest_framework_simplejwt.authentication import JWTAuthentication

from author.serializers import AuthorSerializer
from author.models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    """This endpoint allows post, get, put, patch and delete of author from database"""
    authentication_classes = [JWTAuthentication]
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
