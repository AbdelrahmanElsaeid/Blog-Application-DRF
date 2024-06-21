from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, TagSerializer
from .models import Post, Comment, Category, Tag
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .mypagination import PostPagination


# Create your views here.





class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]     
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['categories', 'tags']

    def perform_create(self, serializer):
        profile = self.request.user.user_profile  
        serializer.save(author=profile)



class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
    def perform_update(self, serializer):
        if self.request.user.user_profile == serializer.instance.author:
            serializer.save()
                            
    def perform_destroy(self, instance):
        if self.request.user.user_profile == instance.author:
            instance.delete()
            

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        profile = self.request.user.user_profile  
        serializer.save(author=profile)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user.user_profile == serializer.instance.author:
            serializer.save()
                            
    def perform_destroy(self, instance):
        if self.request.user.user_profile == instance.author:
            instance.delete()


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer