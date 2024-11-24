from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # The title of the book, max length of 200 characters
    author = models.CharField(max_length=100)  # The author of the book, max length of 100 characters
    publication_year = models.IntegerField()  # The year of publication, an integer

    def __str__(self):
        return self.title

# Create your models here.
