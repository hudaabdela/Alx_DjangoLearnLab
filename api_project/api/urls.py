# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Update the URL patterns to include the router URLs for CRUD operations
urlpatterns = [
    path('', include(router.urls)),  # This includes all routes registered with the router
]


