from django.contrib import admin
from .models import Book

from .models import Book

# Define a custom admin class
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Fields to filter by in the sidebar
    list_filter = ('publication_year',)

    # Enable search functionality on title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
# Register your models here.
