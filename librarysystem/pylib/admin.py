from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class Book_admin(admin.ModelAdmin):
    list_display = ['id','isbn','name','author','category']