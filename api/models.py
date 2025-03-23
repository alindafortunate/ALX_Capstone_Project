from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    ISBN=models.CharField(max_length=255, unique=True)
    number_of_copies_available=models.IntegerField()
    


class Transcations(models.Model):
    pass
