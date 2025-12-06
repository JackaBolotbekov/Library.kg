from django.shortcuts import render, get_object_or_404
from .models import Book

# 1. Вывод списка всех книг
def book_list_view(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('-id')
        return render(request, 'books.html', {'books': books})

# 2. Вывод детальной информации об одной книге 
def book_detail_view(request, id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=id) 
        return render(request, 'book_detail.html', {'book': book})