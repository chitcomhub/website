from django import forms

from .models import Chiter

class PostForm(forms.ModelForm):

    class Meta:
        model = Chiter
        fields = ('name', 'nickname', 'direction', 'technology')