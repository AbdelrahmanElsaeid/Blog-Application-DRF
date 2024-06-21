from rest_framework import serializers
from .models import Post, Category, Tag, Comment, Profile






class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')

    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    comments = CommentSerializer(many=True, read_only=True)
    

    class Meta:
        model = Post
        fields = ['id','title','author', 'content','created_at','updated_at', 'categories', 'tags','comments']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__' 





