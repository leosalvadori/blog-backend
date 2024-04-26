from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        Post.objects.create(title='test title', content='test content', user=user)

    def test_post_creation(self):
        post = Post.objects.get(id=2)
        self.assertEqual(post.title, 'test title')
        self.assertEqual(post.content, 'test content')
        self.assertEqual(post.user.username, 'testuser')
