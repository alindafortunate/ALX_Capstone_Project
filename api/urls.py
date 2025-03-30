from django.urls import path
from .views import (
    index,
    BookListApiView,
    BookCreateApiView,
    BookDetailApiView,
    BookUpdateApiView,
    BookDeleteApiView,
    check_out_a_book,
    return_a_book,
    check_available_books,
)

urlpatterns = [
    path("", index, name="home"),
    path("books/", BookListApiView.as_view(), name="books"),
    path("book/create/", BookCreateApiView.as_view(), name="book-create"),
    path("book/<int:pk>/", BookDetailApiView.as_view(), name="book-detail"),
    path("book/<int:pk>/update/", BookUpdateApiView.as_view(), name="book-update"),
    path("book/<int:pk>/delete/", BookDeleteApiView.as_view(), name="book-delete"),
    path("check_out/<int:id>/", check_out_a_book, name="book_check_out"),
    path("return_book/<int:id>/", return_a_book, name="return_book"),
    path("check_available_books/", check_available_books, name="available_books"),
]
