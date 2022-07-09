# Import mimetypes module

# import os module
import os
from django.http import FileResponse
# Import HttpResponse module
from django.http.response import HttpResponse
from librarysystem.settings import MEDIA_ROOT
from .models import Book

def download_file(request,book_isbn):
    book = Book.objects.get(isbn=book_isbn)
    # get the download path
    
    download_path = os.path.join(MEDIA_ROOT, book.file.name )
    if os.path.exists(download_path):
        file = open(download_path,'rb')
        return FileResponse(file,as_attachment=True)
        # with open(download_path, 'rb') as fh:
            # response = HttpResponse(fh.read(), content_type="application/adminupload")
            # response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            # return response