from django import forms
from task.models import *


class DirectorDetailForm(forms.ModelForm):

    class Meta:
        model = DirectorDetail
        exclude = ['ca']


class StudentBodyDetailForm(forms.ModelForm):

    class Meta:
        model = StudentBodyDetail
        exclude = ['ca']

class ImageUploadForm(forms.ModelForm):
    poster = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Poster
        fields = ['poster']
