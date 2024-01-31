from django.http import HttpResponse
from django.template import loader
from .models import Book, Author


def home(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


def books(request):
    available_books = Book.objects.all().values()
    template = loader.get_template('books.html')
    context = {
    'available_books': available_books, 
    }
    return HttpResponse(template.render(context, request))



def authors(request):
    template = loader.get_template('authors.html')
    return HttpResponse(template.render())
