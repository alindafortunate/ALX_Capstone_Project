from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Book, CheckOuts
from .serializers import BookSerializer, CheckOutsSerializer


def index(request):
    return render(request, "api/home.html")


class BookListApiView(ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]


class BookDetailApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# view for checking out a book.
@api_view(["GET"])
def check_out_a_book(request, id):
    try:

        book = Book.objects.get(id=id)

        if book.check_out_book() == True:
            serializer = BookSerializer(book)
            book.number_of_copies_available -= 1

            return Response(f"{book.title} by {book.author} checked_out enjoy reading")
        else:
            return Response("Book not available currently, re-check in a few days.")
    except Book.DoesNotExist:
        return Response("Sorry book not available")


@api_view(["GET"])
def return_a_book(request, id):
    try:
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        if book.return_book():
            return Response("Thank you for reading and returning the book.")
        else:
            return Response("Book had not been checked out.")
    except Book.DoesNotExist:
        return Response("Sorry book currently not available.")


@api_view(["GET"])
def check_available_books(request):
    try:
        book = Book.objects.filter(number_of_copies_available__gte=1)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response("No book copies available")


class CheckOutListApiView(ListAPIView):
    queryset = CheckOuts.objects.all()
    serializer_class = CheckOutsSerializer
