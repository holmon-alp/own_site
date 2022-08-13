from django import forms
from django.forms import ModelForm
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')



class PostForm(ModelForm):

    class Meta:
        model = BlogPost
        fields = ["title", "image", "about"]