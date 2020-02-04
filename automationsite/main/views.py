from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.views import generic
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status='a').count()
    num_authors = Author.objects.count()
    num_genres_fiction = Book.objects.filter(genre=1).count()
    num_genres_nonfiction = Book.objects.filter(genre=2).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_fiction': num_genres_fiction,
        'num_genres_nonfiction': num_genres_nonfiction,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'
    queryset = Book.objects.all()
    template_name = 'book_list.html'
    paginate_by = 1


class BookDetailView(generic.DetailView):
        model = Book
        template_name = 'book_detail.html'

