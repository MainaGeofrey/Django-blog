from pyexpat import model
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    #Django handles form processing and validation
    class Meta:
        model = Comment
        #by default django will generate all fields from the model
        #but we can define the fields we want explicitly
        fields = ('name', 'email', 'body')