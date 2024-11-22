from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Existing views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Secured book views
    path('books/add/', views.add_book, name='add_book'),  # Adding a book
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),  # Editing a book
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),  # Deleting a book
]
