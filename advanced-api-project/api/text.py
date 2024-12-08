# api/models.py

"""
Author Model:
- name: Stores the author's name as a string.
- __str__: Returns the author's name for readability.

Book Model:
- title: Stores the book's title as a string.
- publication_year: An integer field for the year the book was published.
- author: A foreign key to Author, establishing a one-to-many relationship.
- __str__: Returns the book's title for readability.
"""

# api/serializers.py

"""
BookSerializer:
- Serializes all fields from the Book model.
- Adds custom validation to ensure publication_year is not in the future.

AuthorSerializer:
- Serializes the author's name and a nested list of books using BookSerializer.
- Demonstrates handling a one-to-many relationship.
"""
