from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author.username, "testuser")

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)
        self.comment = Comment.objects.create(post=self.post, author="Commenter", text="Nice Post!")

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, "Nice Post!")
        self.assertEqual(self.comment.post.title, "Test Post")
