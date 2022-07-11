from django.shortcuts import render
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
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