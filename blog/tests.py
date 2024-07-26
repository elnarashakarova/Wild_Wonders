from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone
import textwrap

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(
            author = self.user,
            title = 'Test Post',
            text = 'This is the content of the test post',
            created_date = timezone.now(),
            published_date= timezone.now()         
        )

    def test_create_post(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(str(self.post), self.post.title)

    #############################################
    
    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)

class PostURLTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(
            author=self.user,
            title='Test Post',
            text='This is a test post. It should be long enough to create an excerpt.',
            created_date=timezone.now(),
            published_date=timezone.now()
        )
        
    def test_post_list_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_post_detail_url(self):
        response = self.client.get(f'/post/{self.post.pk}/')
        self.assertEqual(response.status_code, 200)