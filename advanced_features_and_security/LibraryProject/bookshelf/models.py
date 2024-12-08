from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)


# Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Unique email field
    date_of_birth = models.DateField(null=True, blank=True)  # Optional date of birth
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)  # Optional profile photo

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.CharField(max_length=100)  # Author of the book
    publication_year = models.IntegerField()  # Year of publication
    class Meta:
        permissions = [
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        ]
    def __str__(self):
        return self.title

# Create your models here.
