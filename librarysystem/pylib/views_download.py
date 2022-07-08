# Import mimetypes module

# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
from .models import Book

def download_file(request,book_isbn):
    book = Book.objects.get(isbn=book_isbn)
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT,{{ book.file}} )
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response