from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book
from django.conf import settings

user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Book Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')

# Register models with the admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)

