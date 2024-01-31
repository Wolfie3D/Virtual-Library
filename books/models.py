from django.db import models

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    
    def __repr__(self):
        return f"<Author {self.author_id}: {self.name}>"


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    
    def __repr__(self):
        return f"<book {self.book_id}: {self.title}>"
