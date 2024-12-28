from rest_framework import viewsets, permissions
from rest_framework import filters  # Add filter functionality
from django_filters.rest_framework import DjangoFilterBackend  # For advanced filtering
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'content']  
    ordering_fields = ['created_at', 'updated_at']  
    ordering = ['-created_at']  

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        post = serializer.validated_data['post']
        serializer.save(author=self.request.user, post=post)

# Create your views here.
