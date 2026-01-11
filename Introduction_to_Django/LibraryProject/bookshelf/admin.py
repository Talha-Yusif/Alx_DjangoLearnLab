from django.contrib import admin
from .models import Book

class BookAmdin(admin.ModelAdmin):
    list_display=('title','order','publication_year')
    search_fields=('title')
    list_filter=('title','publication_year')
