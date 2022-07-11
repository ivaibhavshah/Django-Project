from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email",widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label = "First name",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label = "Last name",widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", )
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label = "Email",widget=forms.TextInput(attrs=  {'class':'form-control'}))
    first_name = forms.CharField(label = "First name",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label = "Last name",widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email","first_name","last_name")

   