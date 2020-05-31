from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blog_list.html'
    context_object_name = 'all_posts_list' # new

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'all_posts_detail'