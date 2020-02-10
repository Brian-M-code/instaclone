from django import forms
from .models import Image, Profile, Comments

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes', 'user']
