from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework import filters

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
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UserPassesTestMixin, UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def test_func(self):
        return self.get_object().author == self.request.user


class BookDeleteApiView(UserPassesTestMixin, DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def test_func(self):
        return self.get_object().author == self.request.user


@api_view(["GET"])
def check_out_a_book(request, id):
    try:
        book = Book.objects.get(id=id)
        if book.check_out_book():
            serializer = BookSerializer(book)
            message = {
                "message": f"Requested book: {serializer.data['title']}, has been checked_out.",
            }
            return Response(message)
        else:
            message = {
                "message": "Book copies not available currently, re-check in a few days.",
            }
            return Response(message)
    except Book.DoesNotExist:
        message = {
            "message": "Sorry book not available",
        }
        return Response(message)


@api_view(["GET"])
def return_a_book(request, id):
    try:
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        if book.return_book():
            message = {
                "sucess": f"{serializer.data['title']} returned. Thank you for reading."
            }
            return Response(message)
        else:
            message = {
                "message": "Book had not been checked out.",
            }
            return Response(message)
    except Book.DoesNotExist:
        message = {
            "message": "Sorry book currently not available.",
        }
        return Response(message)


class Check_Available_Books(ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]
    serializer_class = BookSerializer

    def get_queryset(self):
        book = Book.objects.filter(number_of_copies_available__gte=1)
        return book


class CheckOutListApiView(ListAPIView):
    queryset = CheckOuts.objects.all()
    serializer_class = CheckOutsSerializer
