import json
from http.client import HTTPResponse

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from blog.models import Post
from blog.serializers import PostSerializer


@api_view(['GET'])

def home(request):
    posts = PostSerializer(Post.objects.all(), many=True)
    return JsonResponse(posts.data, safe=False)


# Create your views here.
