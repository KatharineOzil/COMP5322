from django.shortcuts import render
from .models import Article, Comment, Category, User
from .forms import CommentForm, SearchForm
from itertools import chain
from django.db.models import Q
from django.http import Http404

# Create your views here.

def index(request):
	return_result = {}
	f = SearchForm()
	return_result.update({'form': f})
	try:
		post = Article.objects.all()
		return_result.update({'result': post})
	except Article.DoesNotExist:
		return_result.update({'result': 'No Result!'})
	return render(request, 'blog/index.html', return_result)

def detail(request, id):
	try:
		post = Article.objects.get(id=id)
		if post.visible == True:
			comments = post.comment_set.all()
			#comments = Comment.objects.filter(article_id=id, status=True)
			if request.method == 'GET':
				f = CommentForm()
				print comments
				return render(request, 'blog/article.html', {'form': f, 'post': post, 'comments': comments})
			elif request.method == 'POST':
				f = CommentForm(request.POST)
				if f.is_valid():
					author = f.cleaned_data['author']
					content = f.cleaned_data['content']
					email = f.cleaned_data['email']
					Comment.objects.create(content=content, author=author, article_id=id, email=email)
					f = CommentForm()
					return render(request, 'blog/article.html', {'form': f, 'post': post, 'comments': comments})
			else:
				f = CommentForm()
				return render(request, 'blog/article.html', {'form': f, 'post': post, 'comments': comments})
		else:
			raise Http404("Article does not exist")

	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	return render(request, 'blog/article.html', {'post': post, 'comments': comments, 'form': f})

def search(request):
	return_result = {}
	if request.method == 'GET':
		f = SearchForm()
		return_result.update({'form': f})
		return render(request, 'blog/search.html', return_result)	
	elif request.method == 'POST':
		f = SearchForm(request.POST)
		if f.is_valid():
			search = f.cleaned_data['search']
			return_article = Article.objects.filter( Q(title__contains=search) | Q(content__contains=search))
			return_result.update({'form': f, 'result': return_article})
			return render(request, 'blog/search.html',return_result)
		else:
			return render(request, 'blog/index.html', {'form': f})

def intro(request):
	try:
		users = User.objects.all()
	except User.DoesNotExist:
		raise Http404("User does not exist!")
	return render(request, 'blog/intro.html', {'users': users})

def archives(request):
	a = {}
	articles = Article.objects.all()
	for c in articles:
		a[c.category.category] = []

	for c in articles:
		a[c.category.category].append(c)
		
	return render(request, 'blog/archives.html', {'a': a})

