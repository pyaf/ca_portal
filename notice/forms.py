from django import forms

form notice.models import Poster


class ImageUploadForm(forms.ModelForm):
    poster = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Poster
        fields = ['poster']
