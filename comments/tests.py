from django.test import TestCase
from .models import Comment
from posts.models import Post
from django.contrib.auth.models import User


class CommentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        post = Post.objects.create(title='test title', content='test content', user=user)
        Comment.objects.create(post=post, user=user, comment='test comment')

    def test_comment_creation(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.post.title, 'test title')
        self.assertEqual(comment.comment, 'test comment')
        self.assertEqual(comment.user.username, 'testuser')
