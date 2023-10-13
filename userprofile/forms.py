from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfiles

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')


    class Meta:
        model = User
        fields =['username','email']
        label ={'username':'USERNAME'}


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfiles
        fields = ['address','phone']
          




