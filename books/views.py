from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from django.contrib import messages


def index(request):
    context = {}
    return render(request, 'index.html', context)


def books(request):
    available_books = Book.objects.all().values()
    context = {'available_books': available_books}
    return render(request, "books.html", context)


def authors(request):
    available_authors = Author.objects.all().values()
    context = {'available_authors': available_authors}
    return render(request, "authors.html", context)


def book_details(request, id):
    book = Book.objects.get(pk=id)
    context = {"book": book}
    return render(request, "book_details.html", context)


def author_details(request, id):
    author = Author.objects.get(pk=id)
    context = {"author": author}
    return render(request, "author_details.html", context)


def insertauthor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        country = request.POST.get('country')
        genre = request.POST.get('genre')
        query = Author(name=name, gender=gender, age=age,
                       country=country, genre=genre)
        query.save()
        messages.success(request, "Author Inserted Successfully")
        return redirect('authors')
    return render(request, "authorInsert.html")


def insertbook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        isbn = request.POST.get('isbn')
        author = request.POST.get('author')
        author = get_object_or_404(Author, name=author)
        query = Book(title=title, isbn=isbn, author=author)
        query.save()
        messages.success(request, "Book Inserted Successfully")
        return redirect('books')

    authors = Author.objects.values_list('name', flat=True)
    context = {"authors": authors}
    return render(request, "bookInsert.html", context)


def update_author(request, id):
    id = int(id)
    author = Author.objects.all()[id]
    if request.method == "POST":
        title = request.POST.get('title')
        isbn = request.POST.get('isbn')
        author = request.POST.get('author')
        author = get_object_or_404(Author, name=author)
        query = Author(title=title, isbn=isbn, author=author)
        query.update()
        messages.success(request, "Book has been Updated Successfully")
        return redirect('authors')
    context = {"author": author}
    return render(request, "update_author.html", context)



def update_book(request, id):
    id = int(id)
    book = Book.objects.all()[id]
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_isbn = request.POST.get('isbn')
        new_author_name = request.POST.get('author')

        book.title = new_title
        book.isbn = new_isbn
        book.author = new_author_name
        book.save()

        messages.success(request, "Book has been updated successfully")
        return redirect('books')
    
    context = {"book": book}
    return render(request, "update_book.html", context)
