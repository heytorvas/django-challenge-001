from rest_framework import  serializers
from django.contrib.auth.models import User

# Register serializer
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password')
        extra_kwargs = {
            "email": {"required": True},
            "password": {"required": True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password')