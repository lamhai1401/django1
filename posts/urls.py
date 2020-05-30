# posts/urls.py
from django.urls import path
from posts.views import HomeView, index

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('celery/', index,  name='celery_test_url'),
]