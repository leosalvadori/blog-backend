from django.urls import path
from posts.views import PostListView, PostCreateView, DeletePostView, PostUpdateView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='list-posts'),
    path('posts/create/', PostCreateView.as_view(), name='create-posts'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='update-posts'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
]
