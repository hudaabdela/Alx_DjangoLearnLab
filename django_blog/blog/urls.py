from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),  # List all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View post details
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete a post
    path('register/', views.register, name='register'),  # User registration
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),  # User login
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),  # User logout
    path('profile/', views.profile, name='profile'),  # User profile
]
