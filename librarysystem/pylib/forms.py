from django import forms
from .models import Book

class AddDataForm(forms.ModelForm):
    file = forms.FileField(label = "Upload book",widget=forms.FileInput(attrs={'name':'myfile'}))
    class Meta:

        model = Book
        fields ="__all__"
