from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Book
from .serializers import BookSerializer


# Create your views here.
def index(request):
    return render(request, "api/home.html")


class BookListApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
