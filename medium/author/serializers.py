from rest_framework import serializers
from author.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'picture']
        extra_kwargs = {
            "name": {"required": True},
            "picture": {"required": True}
        }