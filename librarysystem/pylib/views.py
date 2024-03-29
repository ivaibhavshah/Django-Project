from audioop import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from .forms import AddDataForm
from urllib import request
from django.shortcuts import render, redirect
from .models import Book
from django.conf import settings
# Create your views here.

# To render home page
def home(request):
    return render(request,'pylib/home.html')

# to show all books
def books(request):
    
    if request.user.is_authenticated:
        books = Book.objects.all()
        return render(request,'pylib/books.html', {"books":books})
    else:
        return redirect("login")

# to render 1 book
def detail(request,book_isbn):
    book = Book.objects.get(isbn = book_isbn)
    return render(request,'pylib/detail.html',{"book":book})

#contact us page
def contactus(request):
    return render(request,'pylib/contactus.html')

#adding new books

def adddata(request):
    form = AddDataForm()  
    if request.method =="POST":        
        form = AddDataForm(request.POST, request.FILES)
        if form.is_valid(): 
            data = Book()
            data.isbn = form.cleaned_data["isbn"]
            data.name = form.cleaned_data["name"]
            data.author = form.cleaned_data["author"]
            data.summary = form.cleaned_data["summary"]
            data.category = form.cleaned_data["category"]
            data.image = form.cleaned_data["image"]
            data.file = form.cleaned_data["file"]
            form.save()
            messages.success(request,("Your Book has been added"))
            return redirect('books')
        else:
        
            messages.error(request,("Check your Book Details"))
            return render(request,'pylib/adddata.html',{"form":form })
    else:
        return render(request,'pylib/adddata.html',{"form":form })
        



#searching book
def searchbooks(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books = Book.objects.filter(name__contains=searched)
        return render(request,'pylib/search_book.html',{"searched":searched,"books":books})        
    return render(request,'pylib/search_book.html')