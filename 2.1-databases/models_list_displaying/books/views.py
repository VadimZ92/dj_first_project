from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

def books_home(request):
    template = 'books/books.html'
    all_books = Book.objects.all()
    context = {
        "book": all_books
    }
    return render(request, template, context)

def books_view(request):
    template = 'books/books_list1.html'
    all_books = Book.objects.all()
    context = {
        "book": all_books
    }
    return render(request, template, context)

def books_filter(request):
    template = 'books/books_list1.html'
    all_books = Book.objects.all()
    page_date = int(request.GET.get('page', 1))
    paginator = Paginator(all_books, 10)
    page = paginator.get_page(page_date)
    books_f = Book.objects.filter(pub_date="2021-09-18")
    context = {
        "book": books_f,
        'page': page,
    }
    return render(request, template, context)
