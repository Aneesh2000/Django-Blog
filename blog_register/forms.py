from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {
            'title': 'Title',
            'description': 'Description',
            'auth_name':'Auther',
            # 'img':'Image'
        }
    