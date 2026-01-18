from django.urls import path
from .views import book_list, BookDetailView
urlpatterns=[
    path('books/',book_list,name="book_list"),
    path('books/<int:pk>/',BookDetailView.as_view(),name="book_details")
]