from pyexpat import model

from attr import fields
from .models import Comment, Image
from django import forms


class CommentForm(forms.ModelForm):
    #Django handles form processing and validation
    class Meta:
        model = Comment
        #by default django will generate all fields from the model
        #but we can define the fields we want explicitly
        fields = ('name', 'email', 'body')
        

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    
    class Meta:
        model = Image
        fields = ('title', 'image')