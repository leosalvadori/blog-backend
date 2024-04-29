from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from posts.models import Post
from comments.serializers import CommentSerializer
from comments.models import Comment
from django.shortcuts import get_object_or_404


class CommentCreateAPIview(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = self.get_object()
        serializer.save(user=self.request.user, post=post)


class CommentListAPIview(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        post_pk = self.kwargs['pk']
        get_object_or_404(Post, pk=post_pk)
        return Comment.objects.filter(post=post_pk)
