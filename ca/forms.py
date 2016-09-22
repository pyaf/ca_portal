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


class ProfileUpdateForm(forms.Form):

    name = forms.CharField(label="Name",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','placeholder':'Name',}))

    year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'required':'true', }),choices=year_choices,)

    mobile_number = forms.IntegerField(label="Mobile Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'number', 'required':'true','placeholder':"Mobile Number"}))

    whatsapp_number = forms.IntegerField(label="WhatsApp Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'number', 'required':'true','placeholder':"WhatsApp Number"}))

    postal_address = forms.CharField(label="Postal Address",
                               widget=forms.Textarea(attrs={'class': 'form-control','type':'textarea','rows': '5', 'placeholder':"Postal Address"}))

    pincode = forms.CharField(label="Pincode",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'number', 'placeholder':"Postal Address"}))
