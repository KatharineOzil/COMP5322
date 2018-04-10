from django import forms
from .models import Article, Comment, Category
from django.utils.safestring import mark_safe

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content', 'author']

class SearchForm(forms.Form):
	search = forms.CharField(max_length=200)