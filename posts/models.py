from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATE_MAPPING = (
        ("draft", "draft"),
        ("published", "published")
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_posts')
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATE_MAPPING, default='draft')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.title}'
