from django.contrib.auth.models import User
from django import forms
from ca.models import Poster, CAProfile, year_choices

year_choices_empty = [('','Year ')] + year_choices

class ImageUploadForm(forms.ModelForm):
    poster = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Poster
        fields = ['poster']
