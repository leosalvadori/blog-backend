from django.urls import path
from comments.views import AddCommentView, ListCommentsView


urlpatterns = [
    path('posts/<int:pk>/add_comment/', AddCommentView.as_view(), name='add-comment'),
    path('posts/<int:pk>/comments/', ListCommentsView.as_view(), name='list_comments'),
]
