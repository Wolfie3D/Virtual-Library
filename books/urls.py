from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("books/", views.books, name='books'),
    path("authors/", views.authors, name='authors'),
    path('insertauthor/', views.insertauthor, name="insertauthor"),
    path('insertbook/', views.insertbook, name="insertbook"),
    path('book/<id>', views.book_details, name="book_details"),
    path('author/<id>', views.author_details, name="author_details"),
    path('update_author/<id>/', views.update_author, name='update_author'),
    path('update_book/<id>/', views.update_book, name='update_book'),
]
