from django.urls import path, include
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('new/', BlogCreateView.as_view(), name='post_new'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blogDetail'),
    path('list/', BlogListView.as_view(), name='blogList'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='post_delete'),
]
