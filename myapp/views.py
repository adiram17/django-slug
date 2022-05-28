from django.shortcuts import render
from .models import Book

def book(request, slug):
    book = Book.objects.filter(slug = slug).first()
    return render(request, 'book.html', { 'book' : book })