from django import forms


from django import forms
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    isbn = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    summary = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=200,blank = True)
    image = models.ImageField(upload_to='book_images')
    file = models.FileField(null=True,upload_to="bookpdf")
    def __str__(self):
        return f"ISBN : {self.isbn}, Name : {self.name}, Author : {self.author}, Summary : {self.summary}, Image : {self.image},file : {self.file}"