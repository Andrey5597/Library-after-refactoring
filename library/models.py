from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Shelf(models.Model):
    shelf_name = models.CharField(max_length=2, null=True, verbose_name='Shelf number')

    def __str__(self):
        return self.shelf_name

    class Meta:
        verbose_name_plural = 'Shelves'


class Book(models.Model):
    book_title = models.CharField(max_length=50, verbose_name='Title')
    isbn = models.CharField(max_length=13, verbose_name='ISBN')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Author')
    published = models.DateField(verbose_name='Date of publish')
    number_of_pages = models.IntegerField(verbose_name='Number of pages')
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    book_summary = models.TextField(max_length=1500, verbose_name='Book summary')
    shelf = models.ForeignKey('Shelf', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse('book-info', args=[str(self.pk)])


class Author(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    surname = models.CharField(max_length=20, verbose_name='Surname')
    date_of_birth = models.DateField(verbose_name='Date of birth', null=True, blank=True)
    date_of_death = models.DateField(verbose_name='Date of death', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Genre(models.Model):
    genre = models.CharField(max_length=20, verbose_name='Genre')

    def __str__(self):
        return self.genre


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='a')
    borrowed = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    class Meta:
        ordering = ['due_back']
        permissions = (("can_see_all_rented_books", "List of rented books"),)

    def __str__(self):
        return self.book.book_title

    def get_absolute_url(self):
        return reverse('copy_update', args=[str(self.pk)])


