from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("books/", views.books, name='books'),
    path("authors/", views.authors, name='authors'),
    path('authors/insertauthor/',views.insertauthor,name="insertauthor"),
    path('books/insertbook/',views.insertbook,name="insertbook"),
    # path('update/<id>',views.updateData,name="updateData"),
    # path('delete/<id>',views.deleteData,name="deleteData"),
]
