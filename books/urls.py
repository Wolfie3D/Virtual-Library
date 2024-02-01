from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("books/", views.books, name='books'),
    path("authors/", views.authors, name='authors'),
    path('insertauthor/', views.insertauthor, name="insertauthor"),
    path('insertbook/', views.insertbook, name="insertbook"),
    # path('update_author/<author_id>/', views.update_author, name='update_author'),
    # path('delete/<id>',views.deleteData,name="deleteData"),
]
