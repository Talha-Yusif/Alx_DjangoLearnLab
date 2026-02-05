from django.contrib import admin
from .models import Book

class BookAmdin(admin.ModelAdmin):
    list_display=('title','author','publication_year')
    search_fields=('title','publication_year')
    list_filter=('title','publication_year')
admin.site.register(Book,BookAmdin)