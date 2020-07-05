from django import forms
from .models import Post


class add_post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        labels = {
            'title': '',
            'content': '',
            'image': '',
        }