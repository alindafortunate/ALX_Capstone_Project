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


class Transcations(models.Model):
    pass
