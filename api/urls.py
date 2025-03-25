from django.urls import path
from .views import (
    BookListApiView,
    BookCreateApiView,
    BookDetailApiView,
    BookUpdateApiView,
    BookDeleteApiView,
)

urlpatterns = [
    path("books/", BookListApiView.as_view(), name="books"),
    path("book/create/", BookCreateApiView.as_view(), name="book-create"),
    path("book/<int:pk>/", BookDetailApiView.as_view(), name="book-detail"),
    path("book/<int:pk>/update/", BookUpdateApiView.as_view(), name="book-update"),
    path("book/<int:pk>/delete/", BookDeleteApiView.as_view(), name="book-delete"),
]
