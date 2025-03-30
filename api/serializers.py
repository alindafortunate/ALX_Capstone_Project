from rest_framework import serializers
from .models import Book, CheckOuts


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CheckOutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOuts
        fields = "__all__"
