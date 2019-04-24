from django.test import TestCase

from ..models import Shelf, Book, Author, Genre, BookInstance


class ShelfModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Shelf.objects.create(shelf_name='A1')

    def test_shelf_name_max_length(self):
        shelf_name = Shelf.objects.get(id=1)
        max_length = shelf_name._meta.get_field('shelf_name').max_length
        self.assertEqual(max_length, 2)

    def test_shelf_name_label(self):
        shelf_name = Shelf.objects.get(id=1)
        field_label = shelf_name._meta.get_field('shelf_name').verbose_name
        self.assertEqual(field_label, 'Shelf number')

    def test_object_name_is_shelf_name(self):
        shelf_name = Shelf.objects.get(id=1)
        expected_name = 'A1'
        self.assertEqual(expected_name, str(shelf_name))


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(book_title='Harry Potter',
                            isbn=1234567890123, published='2003-06-21',
                            number_of_pages=766, book_summary='Cool',
                            author=Author.objects.create(name='Will', surname='Smith'),
                            genre=Genre.objects.create(genre='Novel'),
                            shelf=Shelf.objects.create(shelf_name='C3', id=2)
                            )

    def test_book_title_max_length(self):
        book_title = Book.objects.get(id=1)
        max_length = book_title._meta.get_field('book_title').max_length
        self.assertEqual(max_length, 50)

    def test_book_title_label(self):
        book_title = Book.objects.get(id=1)
        field_label = book_title._meta.get_field('book_title').verbose_name
        self.assertEqual(field_label, 'Title')

    def test_isbn_max_length(self):
        isbn = Book.objects.get(id=1)
        max_length = isbn._meta.get_field('isbn').max_length
        self.assertEqual(max_length, 13)

    def test_isbn_label(self):
        isbn = Book.objects.get(id=1)
        field_label = isbn._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_author_label(self):
        author = Book.objects.get(id=1)
        field_label = author._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'Author')

    def test_published_label(self):
        published = Book.objects.get(id=1)
        field_label = published._meta.get_field('published').verbose_name
        self.assertEqual(field_label, 'Date of publish')

    def test_number_of_pages_label(self):
        number_of_pages = Book.objects.get(id=1)
        field_label = number_of_pages._meta.get_field('number_of_pages').verbose_name
        self.assertEqual(field_label, 'Number of pages')

    def test_book_summary_label(self):
        book_summary = Book.objects.get(id=1)
        field_label = book_summary._meta.get_field('book_summary').verbose_name
        self.assertEqual(field_label, 'Book summary')

    def test_book_summary_max_length(self):
        book_summary = Book.objects.get(id=1)
        max_length = book_summary._meta.get_field('book_summary').max_length
        self.assertEqual(max_length, 1500)

    def test_object_name_is_book_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = 'Harry Potter'
        self.assertEqual(expected_object_name, str(book))

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/library/book/1')


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Will', surname='Smith')

    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')

    def test_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 20)

    def test_surname_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('surname').verbose_name
        self.assertEqual(field_label, 'Surname')

    def test_surname_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('surname').max_length
        self.assertEqual(max_length, 20)

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'Date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'Date of death')

    def test_object_name_is_name_space_surname(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.name} {author.surname}'
        self.assertEqual(expected_object_name, str(author))

    def test_object_name_is_name_space_surname1(self):
        author = Author.objects.get(id=1)
        expected_object_name = 'Will Smith'
        self.assertEqual(expected_object_name, str(author))


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(genre='Novel', id=2)

    def test_genre_label(self):
        genre = Genre.objects.get(id=2)
        field_label = genre._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, 'Genre')

    def test_genre_max_length(self):
        genre = Genre.objects.get(id=2)
        max_length = genre._meta.get_field('genre').max_length
        self.assertEqual(max_length, 20)

    def test_object_name_is_genre(self):
        genre = Genre.objects.get(id=2)
        expected_object_name = 'Novel'
        self.assertEqual(expected_object_name, str(genre))


class BookinstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        BookInstance.objects.create(status='a', book=Book.objects.create(book_title='Harry Potter',
                                    isbn=1234567890123, published='2003-06-21',
                                    number_of_pages=766, book_summary='Cool',
                                    author=Author.objects.create(name='Will', surname='Smith'),
                                    genre=Genre.objects.create(genre='Novel'),
                                    shelf=Shelf.objects.create(shelf_name='C3', id=2), id=3
                                    ), due_back='2019-04-26')

    def test_status_max_length(self):
        status = BookInstance.objects.get(id=1)
        max_length = status._meta.get_field('status').max_length
        self.assertEqual(max_length, 1)

    def test_object_name_is_book_title(self):
        book = BookInstance.objects.get(id=1)
        expected_object_name = 'Harry Potter'
        self.assertEqual(expected_object_name, str(book))

    def test_get_absolute_url(self):
        bookinstance = BookInstance.objects.get(id=1)
        self.assertEqual(bookinstance.get_absolute_url(), '/library/copy/1/update/')
