from django.urls import path
from posts.views import PostCreateListView

urlpatterns = [
    path('posts/', PostCreateListView.as_view(), name='posts-create-list')
]
