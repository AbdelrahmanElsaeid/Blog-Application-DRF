from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView, CategoryListView,TagListView



urlpatterns = [
     path('posts/', PostListCreateView.as_view(), name='post-list-create'),
     path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),     
     path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
     path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-delete'),
     path('categories/', CategoryListView.as_view(), name='category-list'),
     path('tags/', TagListView.as_view(), name='tag-list'),
]
