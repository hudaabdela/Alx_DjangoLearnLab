from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # To display the username

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)  # Nested comments in post details

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']
