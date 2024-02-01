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
        isbn = request.POST.get('isbn')
        title = request.POST.get('title')
        query = Book(title=title, isbn=isbn)
        query.save()
        messages.info(request, "Book Inserted Successfully")
        return redirect("books/")
    template = loader.get_template('bookInsert.html')
    return HttpResponse(template.render(request))


def insertauthor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        country = request.POST.get('country')
        genre = request.POST.get('genre')
        if not name or not gender or not age or not country or not genre:
            messages.error(request, "All fields are required.")
            return redirect("authors/")
        query = Author(name=name, gender=gender, age=age,
                       country=country, genre=genre)
        query.save()
        messages.success(request, "Author Inserted Successfully")
        return redirect("authors/")
    template = loader.get_template('authorInsert.html')
    context = {}
    return HttpResponse(template.render(context, request))


# def updateData(request,id):
#     if request.method=="POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         age=request.POST['age']
#         gender=request.POST['gender']

#         edit=Student.objects.get(id=id)
#         edit.name=name
#         edit.email=email
#         edit.gender=gender
#         edit.age=age
#         edit.save()
#         messages.warning(request,"Data Updated Successfully")
#         return redirect("/")

#     d=Student.objects.get(id=id)
#     context={"d":d}
#     return render(request,"edit.html",context)

# def deleteData(request,id):
#     d=Student.objects.get(id=id)
#     d.delete()
#     messages.error(request,"Data deleted Successfully")
#     return redirect("/")
