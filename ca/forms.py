from django.contrib.auth.models import User
from django import forms
from ca.models import *


class PasswordChangeForm(forms.Form):

    oldPassword = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Old password','required':'true', 'type':'password','name': 'oldPassword'}))

    password1 = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'New password','required':'true', 'type':'password','name': 'password1'}))

    password2 = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'New password (repeat)','required':'true', 'type':'password','name': 'password2'}))
