from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import BookForm
from webapp.models import Book


# Create your views here.


def index(request):
    books = Book.objects.order_by('-created_at').filter(statuses='active')
    return render(request, 'index.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            books = Book.objects.order_by('-created_at').filter(statuses='active')
            return render(request, 'index.html', {'book': book, "books": books})
        else:
            return render(request, 'create_book.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'create_book.html', context={"form": form})

def edit_book(request, *args, pk, **kwargs):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            books = Book.objects.order_by('-created_at').filter(statuses='active')
            return render(request, 'index.html', {'book': book, "books": books})
        else:
            return render(request, 'edit_book.html', {'form': form})
    else:
        form = BookForm(instance=book)
        return render(request, 'edit_book.html', context={"form": form})

def delete_book(request, *args, pk, **kwargs):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        check_delete = request.POST.get("check_delete")
        if check_delete == book.email:
            book.delete()
            return redirect("index")
        else:
            return render(request, "delete_book.html", {"book": book,'error': 'Email не совпадает!'})
    else:
        return render(request, 'delete_book.html', {"book": book})

