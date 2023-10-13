from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models





class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user

    # @property
    # def full_name(self):
    #     return self.user.first_name +" "+ self.user.last_name

