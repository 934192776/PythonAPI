from django.contrib.auth.models import User
from rest_framework import permissions

from blog import viewsets, serializers
from blog.models import Post
from blog.serializers import PostSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_superuser




