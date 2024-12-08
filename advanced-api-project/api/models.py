from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Author's full name")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Book's title")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.
