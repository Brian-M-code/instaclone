from django import forms
from .models import Image, Profile, Comments

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes', 'user']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image', 'user']
