from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Author(models.Model):
    name = models.CharField(max_length=100, )
    gender = models.CharField(max_length=10)
    age = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(100)])
    country = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    
    def __repr__(self):
        return f"<{self.name}>"


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    
    
    def __repr__(self):
        return f"<{self.title}>"
