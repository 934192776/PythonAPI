import json
from http.client import HTTPResponse

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status,viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Post, Category
from blog.serializers import PostSerializer, UserSerializer, CategorySerializer


@api_view(['GET'])

def home(request):
    posts = PostSerializer(Post.objects.all(), many=True)
    return JsonResponse(posts.data, safe=False)

@api_view(['GET'])
def author_detail(request, pk):
    author = User.objects.get(id=pk)
    author = UserSerializer(author)
    author = {"id": author.id,
              "username": author.username}
    return JsonResponse(author.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    user = User.objects.get(id=pk)
    user = UserSerSerializer(user)
    return JsonResponse(user.data, safe=False)


@api_view(['POST'])
def register(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        user_object = User.objects.get(username=request.data['username'])
        user_object.set_password(request.data['password'])
        user_object.save()
        user_serializer =UserSerializer(user_object)
        return JsonResponse(user_serializer.data, safe=False)
    return JsonResponse(user_serializer.errors, safe=False)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
