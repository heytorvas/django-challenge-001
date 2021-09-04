from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response

from auth.serializers import AuthSerializer, UserSerializer


class RegisterApi(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthSerializer
    
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(
                user,
                context=self.get_serializer_context()
            ).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })