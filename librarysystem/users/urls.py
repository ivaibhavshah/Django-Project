from pylib.models import *
from django.urls import path
from .views import SignUpView, EditProfileView , PasswordChangeView, PasswordResetView
urlpatterns = [
    path('signup',SignUpView.as_view(),name='signup'), 
    path('my_profile',EditProfileView.as_view(),name="myprofile"),
    path("change_password/",PasswordChangeView.as_view(),name="changepass"),
    path("reset_password/",PasswordResetView.as_view(),name="resetpass"),
    
]