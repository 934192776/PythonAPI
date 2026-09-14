from django.urls import path
from rest_framework import routers

from blog.views import home
from blog.viewsets import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', home, name='home'),
] + router.urls