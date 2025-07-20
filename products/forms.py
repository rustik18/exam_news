from django import forms
from .models import *

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields = ['category', 'title', 'desc', 'image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'info', 'text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text', 'rate']
