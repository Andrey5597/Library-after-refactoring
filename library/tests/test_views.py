from django.test import TestCase
from django.urls import reverse

from ..models import Author, Book, Shelf, Genre, BookInstance


class BookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(book_title='Harry Potter',
                            isbn=1234567890123, published='2003-06-21',
                            number_of_pages=766, book_summary='Cool',
                            author=Author.objects.create(name='Will', surname='Smith'),
                            genre=Genre.objects.create(genre='Novel'),
                            shelf=Shelf.objects.create(shelf_name='C3')
                            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/library/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/book_list.html')


class GenreListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(genre='Novel')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/library/genres/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/genre_list.html')


class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_authors = 10

        for author_id in range(number_of_authors):
            Author.objects.create(
                name=f'Name {author_id}',
                surname=f'Surname {author_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/library/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/author_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 5)

    def test_lists_all_authors(self):
        response = self.client.get(reverse('authors') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 5)


