from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["first_name",'last_name','username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username',}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','image']