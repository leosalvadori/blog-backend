from posts.models import Post
from rest_framework import generics
from posts.serializers import PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied


class PostListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_queryset(self):
        user_posts = self.request.query_params.get('my_posts', None)
        if user_posts is not None and self.request.user.is_authenticated:
            return Post.objects.filter(user=self.request.user)
        return Post.objects.all()


class PostCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeletePostView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("Permission denied!")
        instance.delete()
