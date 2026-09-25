from django.urls import path
from rest_framework import routers

from blog.views import home, author_detail, CategoryViewSet
from blog.viewsets import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('author/<int:pk>',
         author_detail,
         name='author_detail'),
] + router.urls