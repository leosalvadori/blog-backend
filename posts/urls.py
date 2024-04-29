from django.urls import path
from posts.views import PostListAPIView, PostCreateAPIView, PostRetrieveUpdateDeleteAPIView


urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='list-posts'),
    path('posts/create/', PostCreateAPIView.as_view(), name='create-posts'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteAPIView.as_view(), name='retrieve-update-delete-posts'),
]
