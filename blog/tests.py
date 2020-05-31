from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from blog.models import Post
# Create your tests here.

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', 
            email='test@email.com', 
            password='secret',
        )

        self.post = Post.objects.create(
            title='A good title', 
            body='Nice body content', 
            author=self.user,
        )
    
    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self): 
        self.assertEqual(f'{self.post.title}', 'A good title') 
        self.assertEqual(f'{self.post.author}', 'testuser') 
        self.assertEqual(f'{self.post.body}', 'Nice body content')
    
    def test_post_list_view(self):
        resp = self.client.get('/blog/list/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Nice body content')
        self.assertTemplateUsed(resp, 'blog_list.html')
    
    def test_post_detail_view(self):
        resp = self.client.get('/blog/detail/1/')
        no_response = self.client.get('/blog/detail/100000/')
        self.assertEqual(resp.status_code, 200) 
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(resp, 'A good title') 
        self.assertTemplateUsed(resp, 'blog_detail.html')