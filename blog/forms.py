from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content', 'author', 'email']

		content = forms.CharField
'''
	def clean(self):
		try:
			email = self.cleaned_data['email']
		except Exception:
			print 'except: '+ str(Exception)
			raise forms.ValidationError("It requires EMAIL FORMAT")
		return self.cleaned_data
'''
class SearchForm(forms.Form):
	search = forms.CharField(max_length=200, required=True)

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content', 'author', 'email', 'parent']
	'''
	def clean(self):
		try:
			email = self.cleaned_data['email']
		except Exception:
			print 'except: '+ str(Exception)
			raise forms.ValidationError("It requires EMAIL FORMAT")
		return self.cleaned_data
	'''