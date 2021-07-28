from collections import namedtuple
from django.urls import path
from .views import CreatePostView, UpdatePostView, DeletePostView, PostDetailView, \
    AllPostsView, VisiblePostView

urlpatterns = [
    path('', AllPostsView, name='all-posts'),
    path('created-post/', VisiblePostView, name='created-post'),
    path('create-post/', CreatePostView, name='create-post'),
    path('update-post/<int:pk>/', UpdatePostView, name='update-post'),
    path('delete-post/<int:pk>/', DeletePostView, name='delete-post'),
    path('post-detail<int:pk>/', PostDetailView, name='post-detail')
]