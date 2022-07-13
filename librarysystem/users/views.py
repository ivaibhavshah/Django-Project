from django.contrib import messages
from django.shortcuts import render
from .forms import RegisterForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth.forms import UserChangeForm , PasswordResetForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView, PasswordResetView

# Create your views here.

#Change Password
class PasswordChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')
    template_name = 'registration/password_change.html'


#Reset Password
class PasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('home')
    template_name = 'registration/password_change.html'

 #signup form
class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#class for editing profile
class EditProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editprofile.html'
    
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
  