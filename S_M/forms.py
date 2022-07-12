from dataclasses import fields
from django import forms
from . import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('comment',)


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('post',)

class ListPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields= '__all__'