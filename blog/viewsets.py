from rest_framework import viewsets,permissions
from blog.models import Post
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]


    def get_permissions(self):
     if self.action == 'create':
        return [permissions.IsAuthenticated]
     return super().get_permissions()


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

