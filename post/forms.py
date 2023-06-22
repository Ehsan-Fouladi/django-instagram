from django import forms
from .models import Post, Comments


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "caption"]

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]