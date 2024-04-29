from posts.models import Post
from rest_framework import generics
from posts.serializers import PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class PostListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_queryset(self):
        user_posts = self.request.query_params.get('my_posts', None)
        if user_posts is not None and self.request.user.is_authenticated:
            return Post.objects.filter(user=self.request.user)
        return Post.objects.filter(status='published')


class PostCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user=user)
