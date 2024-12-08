from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author
from datetime import datetime

class BookAPITests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name="Test Author")
        self.book_data = {
            'title': "Test Book",
            'publication_year': 2020,
            'author': self.author.id
        }
        self.book = Book.objects.create(**self.book_data)
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.id})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.id})

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(self.create_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Book created successfully!')

    def test_create_book_unauthenticated(self):
        response = self.client.post(self.create_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        updated_data = {'title': 'Updated Book Title'}
        response = self.client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Book updated successfully!')
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_update_book_unauthenticated(self):
        updated_data = {'title': 'Updated Book Title'}
        response = self.client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['message'], 'Book deleted successfully!')
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_search_books_by_author(self):
        response = self.client.get(self.list_url, {'search': 'Test Author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author']['name'], 'Test Author')

    def test_order_books_by_publication_year(self):
        Book.objects.create(title="Another Book", publication_year=2022, author=self.author)
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)

    def test_validate_publication_year_not_future(self):
        future_year_data = {
            'title': 'Future Book',
            'publication_year': datetime.now().year + 1,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, future_year_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Publication year cannot be in the future.', response.data['publication_year'])
