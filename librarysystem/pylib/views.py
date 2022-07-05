from urllib import request
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request,'pylib/home.html', {"books":books})

def detail(request,book_isbn):
    book = Book.objects.get(isbn = book_isbn)
    return render(request,'pylib/detail.html',{"book":book})