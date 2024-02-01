from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Book, Author
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def books(request):
    available_books = Book.objects.all().values()
    template = loader.get_template('books.html')
    context = {
        'available_books': available_books,
    }
    return HttpResponse(template.render(context, request))


def authors(request):
    available_authors = Author.objects.all().values()
    template = loader.get_template('authors.html')
    context = {
        'available_authors': available_authors,
    }
    return HttpResponse(template.render(context, request))


def insertbook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        isbn = request.POST.get('isbn')
        author = request.POST.get('author')
        
        author_instance = Author.objects.get(author_id=author)
        
        query = Book(title=title, isbn=isbn, author=author_instance)
        query.save()
        messages.success(request, "Book Inserted Successfully")
        return redirect('books')
    
    authors = Author.objects.values_list('author_id', flat=True)
    authors_name= Author.objects.values_list('name', flat=True)
    template = loader.get_template('bookInsert.html')
    context = {
        "authors" : authors,
        'authors_name' : authors_name,
        }
    return HttpResponse(template.render(context, request))


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

    template = loader.get_template('authorInsert.html')
    context = {}
    return HttpResponse(template.render(context, request))


# def update_author(request, author_id):
#     author = Author.objects.filter(author_id=author_id).values()

#     if request.method == "POST":
#         name = request.POST.get('name')
#         gender = request.POST.get('gender')
#         age = request.POST.get('age')
#         country = request.POST.get('country')
#         genre = request.POST.get('genre')
        
#         author.name = name
#         author.gender = gender
#         author.age = age
#         author.country = country
#         author.genre = genre
#         author.save()

#         messages.warning(request, "Data Updated Successfully")
#         return redirect('authors')
#     context = {"author": author}
#     return render(request, "updateAuthor.html", context)





# def deleteData(request,id):
#     d=Student.objects.get(id=id)
#     d.delete()
#     messages.error(request,"Data deleted Successfully")
#     return redirect("/")
