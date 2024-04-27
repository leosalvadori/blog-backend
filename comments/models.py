from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True, editable=False, auto_now_add=True, db_index=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.post}'
