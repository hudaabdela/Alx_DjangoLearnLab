#in django shell
#python manage.py shell

#from api.models import Author, Book
#from api.serializers import AuthorSerializer

# Create sample data
"author = Author.objects.create(name="Jane Austen")"
"book = Book.objects.create(title="Pride and Prejudice", publication_year=1813, author=author)"

# Serialize data
"serializer = AuthorSerializer(author)"
"print(serializer.data)"""