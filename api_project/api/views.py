# api/views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Replace the BookList view with BookViewSet to handle CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
