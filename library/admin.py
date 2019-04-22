from django.contrib import admin
from .models import Book, BookInstance, Author, Genre, Shelf


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'shelf', 'isbn',
                    'author', 'published', 'genre', 'number_of_pages')
    list_display_links = ('book_title',)
    search_fields = ('book_title', 'genre', 'author', 'isbn')
    list_filter = ('shelf', 'author', 'genre')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'date_of_birth', 'date_of_death')
    list_display_links = ('name', 'surname')
    search_fields = ('name', 'surname')


class ShelfAdmin(admin.ModelAdmin):
    list_display = ['shelf_name']


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrowed', 'due_back')
    list_display_links = ('book',)
    list_filter = ('status', 'due_back')
    search_fields = ('book',)


admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Shelf, ShelfAdmin)


# Register your models here.
