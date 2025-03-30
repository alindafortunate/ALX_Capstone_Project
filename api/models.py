from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    ISBN = models.CharField(max_length=255, unique=True)
    number_of_copies_available = models.IntegerField()

    def __str__(self):
        return f"{self.title}"

    def check_out_book(self):
        if self.number_of_copies_available >= 1:
            self.number_of_copies_available -= 1

            return True

        else:
            return "Book not available"

    def return_book(self):
        if self.check_out_book() == True:
            self.number_of_copies_available += 1

        else:
            return "Book not check_out"

    def available_books(self):
        if self.check_out_book() == True:
            return self.number_of_copies_available
        else:
            return self.number_of_copies_available


class Transcations:
    book = []

    def add_book(self, book):
        self.book.append(book)
