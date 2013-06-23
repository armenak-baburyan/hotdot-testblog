# -*- coding: utf-8 -*-
from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(max_length=300, widget=forms.Textarea, label='')


class TagSearchForm(forms.Form):
    tag = forms.CharField(max_length=50)