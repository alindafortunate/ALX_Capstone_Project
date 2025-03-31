from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


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

    def return_book(self):
        if self.check_out_book() == True:
            self.number_of_copies_available += 1
            return True


class CheckOuts(models.Model):
    reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="readers")
    book_taken = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="taken_books"
    )
    returned_book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="returned_books"
    )
    borrowed_at = models.DateTimeField()
    return_on = models.DateTimeField()
    issued_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="librarian"
    )
