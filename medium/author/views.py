from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from rest_framework_simplejwt.authentication import JWTAuthentication

from author.serializers import AuthorSerializer
from author.models import Author

# Create your views here.
class ListAuthorAPIView(ListAPIView):
    """This endpoint list all of the available authors from the database"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CreateAuthorAPIView(CreateAPIView):
    """This endpoint allows for creation of a author"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class UpdateAuthorAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific author by passing in the id of the author to update"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class DeleteAuthorAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific author from the database"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
