from django import forms
from .models import Profile, Image, Comment
from django.contrib.auth.models import User



class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'caption') 




class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

    class Meta:
        model = Comment
        fields = ('comment',)               