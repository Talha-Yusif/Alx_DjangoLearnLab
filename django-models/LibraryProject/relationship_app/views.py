
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
#This view should render a simple text list of book titles and their authors.
def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {'books': books})

class BookDetailView(DetailView):
    model = Book
    template_name = "library_detail.html"
