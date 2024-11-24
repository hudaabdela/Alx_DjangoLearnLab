from django import forms
from .models import Book

# Define the BookForm
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']  # Include the fields to be used
