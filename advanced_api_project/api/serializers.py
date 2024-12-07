from rest_framework import serializers
from .models import Book, Author
class BookSerializer(serializers.ModelSerializer):
    class meta :
        model = Book
        fields = ['id', 'title', 'publication_year','author' ]
    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value    
class AuthorSerializer(serializers.ModelSerializer):
    # Nest BookSerializer to include related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
