from django import forms
from task.models import *


class DirectorDetailForm(forms.ModelForm):
    directorDetail = forms.CharField(label="Director Detail",
                               widget=forms.Textarea(attrs={'class': 'form-control','type':'textarea','cols':'30','rows': '5','placeholder':"Provide us contact details of your college's Director."}))


    class Meta:
        model = DirectorDetail
        exclude = ['ca']


class StudentBodyDetailForm(forms.ModelForm):

    studentBodyDetail = forms.CharField(label="Student Detail",
                               widget=forms.Textarea(attrs={'class': 'form-control','type':'textarea','rows': '5','placeholder':"Provide us contact details of your Student body head of your college."}))


    class Meta:
        model = StudentBodyDetail
        exclude = ['ca']


class ImageUploadForm(forms.ModelForm):
    poster = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Poster
        fields = ['poster']
