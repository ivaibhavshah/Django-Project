from pylib.models import *
from django.urls import path
from .views import SignUpView, EditProfileView
urlpatterns = [
    path('signup',SignUpView.as_view(),name='signup'), 
    path('my_profile',EditProfileView.as_view(),name="myprofile")
]
