from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)


class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
