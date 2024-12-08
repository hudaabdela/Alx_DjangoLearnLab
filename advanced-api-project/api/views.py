from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


# List and Create View
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Update View
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """Custom update logic with enhanced response."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(
            {"message": "Book updated successfully!", "data": serializer.data},
            status=status.HTTP_200_OK
        )


# Delete View
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        """Custom delete response message."""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Book deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT
        )

