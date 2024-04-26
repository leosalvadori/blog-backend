from django.urls import path
from posts.views import PostListView, PostCreateView, DeletePostView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='list-posts'),
    path('create-post/', PostCreateView.as_view(), name='create-posts'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
]
