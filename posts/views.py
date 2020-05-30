from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html' 
    context_object_name = 'all_posts_list' # new


from django.http import HttpResponse
from posts.tasks import my_first_task
def index(request):
    my_first_task.delay(3)
    return HttpResponse('response done')