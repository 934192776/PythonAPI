from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'author', 'header_image',  'author_username', 'category_name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


        extra_kwargs = {
            'author_username': {
                'read_only': True,
                'required': False
            },
            'category_name': {
                'read_only': True,
                 'required': False
            }
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']