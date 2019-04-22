from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q


def home(request):
    """select count (book_title) from library_book;"""
    num_books = Book.objects.all().count()

    """select count (id) from library_BookInstance;"""
    num_instances = BookInstance.objects.all().count()

    """ select count (id) from library_BookInstance where status='a'; """
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    """select count (id) from library_Author;"""
    num_authors = Author.objects.all().count()

    """select count (id) from library_genre;"""
    num_genres = Genre.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }
    return render(request, 'home.html', context=context)


def book_list(request):
    query = request.GET.get('q')
    """select * from library_Book;"""
    queryset = Book.objects.all()
    if query:
        queryset = queryset.filter(
            Q(book_title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(author__surname__icontains=query) |
            Q(genre__genre__icontains=query)
        )

    context = {'book_list': queryset}
    return render(request, 'library/book_list.html', context=context)


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    context_object_name = 'Book'
    template_name = 'library/book_info.html'


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'

    """select distinct author_name from library_Book;"""
    queryset = Author.objects.all()

    template_name = 'library/author_list.html'


class GenreListView(generic.ListView):
    model = Genre
    context_object_name = 'genre_list'

    """select (id) from library_genre;"""
    queryset = Genre.objects.all()

    template_name = 'library/genre_list.html'


class BooksRentedByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'library/books_rented_by_user.html'
    context_object_name = 'rent_list'

    def get_queryset(self):
        ''' select * from library_BookInstance inner join auth_user on library_BookInstance.rent_id=auth_user.id
        where library_BookInstance.status='o' order by due_back '''
        return BookInstance.objects.filter(rent=self.request.user.id).filter(status__exact='o').order_by('due_back')


class BooksRentedByUsersListView(PermissionRequiredMixin, generic.ListView):
    permission_required = ('library.can_see_all_rented_books',)
    model = BookInstance
    template_name = 'library/books_rented_by_users.html'
    context_object_name = 'rent_list'

    def get_queryset(self):
        """select * from library_BookInstance where status='o' order by due_back;"""
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


class BookInstanceCreate(CreateView):
    model = BookInstance
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookInstanceUpdate(UpdateView):
    model = BookInstance
    fields = ['due_back', 'status', 'borrowed']
    success_url = reverse_lazy('books')
