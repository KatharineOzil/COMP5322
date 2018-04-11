from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content', 'author', 'email']

class SearchForm(forms.Form):
	search = forms.CharField(max_length=200)

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content', 'author', 'email', 'parent']