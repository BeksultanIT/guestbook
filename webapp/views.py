from django.shortcuts import render

from webapp.models import Book


# Create your views here.


def index(request):
    books = Book.objects.order_by('-created_at').filter(statuses='active')
    return render(request, 'index.html', {'books': books})
