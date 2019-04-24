from django.test import TestCase

from ..models import Shelf, Book, Author, Genre


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
                            genre=Genre.objects.create(genre='Novel')
                            )

    def test_shelf_name_max_length(self):
        book_title = Book.objects.get(id=1)
        max_length = book_title._meta.get_field('book_title').max_length
        self.assertEqual(max_length, 50)

    def test_book_title_label(self):
        book_title = Book.objects.get(id=1)
        field_label = book_title._meta.get_field('book_title').verbose_name
        self.assertEqual(field_label, 'Title')


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






