from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    
    username = forms.CharField(label = "Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = "Email",widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label = "First name",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label = "Last name",widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label = "Set Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = "Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ("username", "email","first_name","last_name" ,"password1","password2")
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    
    username = forms.CharField(label = "Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = "Email",widget=forms.TextInput(attrs=  {'class':'form-control'}))
    first_name = forms.CharField(label = "First name",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label = "Last name",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = "",widget=forms.HiddenInput(attrs={'class':'form-control',"value" : "no password set"}))
    class Meta:
        model = User
        fields = ("username", "email","first_name","last_name")

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = "Old Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label = "Enter New Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label = "Confirm New Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("old_password","new_password1","new_password2")