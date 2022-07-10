from django.urls import path
from . import views , views_download

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.home,name='home'),
    path('books',views.books,name='books'),
    path('book/<book_isbn>',views.detail,name='detail'),
    path('contactus',views.contactus,name='contactus'),
    path('download/<book_isbn>',views_download.download_file,name='download'),
    path('books/adddata',views.adddata,name='adddata'),
    path('myprofile',views.myprofile,name="myprofile")
]

#to load image
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)