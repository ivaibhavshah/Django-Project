from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.home,name='home'),
    path('book/<book_isbn>',views.detail,name='detail'),
    path('aboutus',views.aboutus,name='aboutus')
]

#to load image
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)