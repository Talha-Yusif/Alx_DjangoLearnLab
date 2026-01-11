from django.contrib import admin

class BookAmdin(admin.ModelAdmin):
    list_display=('title','order','publication_year')
    search_fields=('title')
    list_filter=('title','publication_year')
