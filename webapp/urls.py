from django.urls import path

from webapp.views import index, create_book, edit_book, delete_book

urlpatterns = [
    path('', index, name='index'),
    path('add-book', create_book, name='create_book'),
    path('book/<int:pk>/edit', edit_book, name='edit_book'),
    path('book/<int:pk>/delete', delete_book, name='delete_book'),

]