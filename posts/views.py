from posts.models import Post
from rest_framework import generics
from posts.serializers import PostSerializer
from rest_framework.permissions import AllowAny


class PostCreateListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
