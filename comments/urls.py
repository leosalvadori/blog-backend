from django.urls import path
from comments.views import CommentCreateAPIview, CommentListAPIview


urlpatterns = [
    path('posts/<int:pk>/comments/create/', CommentCreateAPIview.as_view(), name='add-comment'),
    path('posts/<int:pk>/comments/list/', CommentListAPIview.as_view(), name='list-comments'),
]
