from .forms import AddDataForm
from urllib import request
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
# Create your views here.
# To render home page
def home(request):
    return render(request,'pylib/home.html')
# to show all books
def books(request):
    books = Book.objects.all()
    return render(request,'pylib/books.html', {"books":books})
# to render 1 book
def detail(request,book_isbn):
    book = Book.objects.get(isbn = book_isbn)
    return render(request,'pylib/detail.html',{"book":book})
#contact us page
def contactus(request):
    return render(request,'pylib/contactus.html')

#adding new books

def adddata(request):
    submitted = False
    form = AddDataForm()  
    if request.method =="POST":
        form = InputDataForm(request.POST)
    else:
        submitted = False
        return render(request,'pylib/adddata.html',{"form":form , "submitted" : submitted})

