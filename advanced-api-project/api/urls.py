# api/urls.py

from django.urls import path
from .views import BookListCreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),
]
