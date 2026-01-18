
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView

def book_list(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {'books': books})

class BookDetailView(DetailView):
    model = Book
    template_name = "library_detail.html"
