from django.urls import path, include
from blog.views import BlogListView, BlogDetailView

urlpatterns = [
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blogDetail'),
    path('list/', BlogListView.as_view(), name='blogList'),
]
