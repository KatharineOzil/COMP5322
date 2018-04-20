from django.shortcuts import render, render_to_response
from .models import Article, Comment, Category, User
from .forms import CommentForm, SearchForm, ReplyForm
from itertools import chain
from django.db.models import Q
from django.http import Http404

# Create your views here.

def index(request):
	return_result = {}
	f = SearchForm()
	category = Category.objects.all()
	return_result.update({'form': f, 'category': category})
	try:
		post = Article.objects.filter(visible=True).order_by('-created_time')[0: 10]
		return_result.update({'result': post})
	except Article.DoesNotExist:
		return_result.update({'result': 'No Result!'})
	return render(request, 'blog/index.html', return_result)

def detail(request, id):
	try:
		post = Article.objects.get(id=id)
		if post.visible == True:
			comments = post.comment_set.filter(status=True)
			if request.method == 'GET':
				f = CommentForm()
				r_f = ReplyForm()
				return render(request, 'blog/article.html', {'form': f, 'post': post, 'comments': comments, 'replyform': r_f})
			elif request.method == 'POST':
				if 'comment' in request.POST:
					f = CommentForm(request.POST)
					r_f = ReplyForm()
					if f.is_valid():
						author = f.cleaned_data['author']
						content = f.cleaned_data['content']
						email = f.cleaned_data['email']
						Comment.objects.create(content=content, author=author, article_id=id, email=email)
						f = CommentForm()
						return render(request, 'blog/article.html', {'form': f, 'post': post, 'comments': comments, 'replyform': r_f})
				elif 'reply' in request.POST:
					f = CommentForm()
					r_f = ReplyForm(request.POST)
					if r_f.is_valid():
						author = r_f.cleaned_data['author']
						content = r_f.cleaned_data['content']
						email = r_f.cleaned_data['email']
						parent = r_f.cleaned_data['parent']
						Comment.objects.create(content=content, author=author, article_id=id, parent_id=parent.id, email=email)
						r_f = ReplyForm()
						return render(request, 'blog/article.html', {'form': f, 'post': post, 'comments': comments, 'replyform': r_f})
			else:
				f = CommentForm()
				r_f = ReplyForm()
				return render(request, 'blog/article.html', {'form': f, 'post': post, 'comments': comments, 'replyform': r_f})
		else:
			return render_to_response('blog/404.html', {})

	except Article.DoesNotExist:
		return render_to_response('blog/404.html', {})

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
			return_article = Article.objects.filter(Q(title__contains=search) | Q(content__contains=search) | Q(category__category__icontains=search)).filter(visible=True).order_by('-created_time')
			return_result.update({'form': f, 'result': return_article})
			return render(request, 'blog/search.html',return_result)
		else:
			return_result = {}
			f = SearchForm(request.POST)
			category = Category.objects.all()
			return_result.update({'form': f, 'category': category})
			try:
				post = Article.objects.filter(visible=True).order_by('-created_time')[0: 11]
				return_result.update({'result': post})
			except Article.DoesNotExist:
				return_result.update({'result': 'No Result!'})
			return render(request, 'blog/index.html', return_result)

	return render(request, 'blog/search.html', return_result)

def intro(request):
	try:
		users = User.objects.all()
	except User.DoesNotExist:
		raise Http404("User does not exist!")
	return render(request, 'blog/intro.html', {'users': users})

def archives(request):
	a = {}
	articles = Article.objects.filter(visible=True).order_by('-created_time')
	for c in articles:
		a[c.category.category] = []

	for c in articles:
		a[c.category.category].append(c)

	category = Category.objects.all()

	return render(request, 'blog/archives.html', {'a': a, 'category': category})

def category(request, id):
	category = Category.objects.get(id=id)
	articles = Article.objects.filter(visible=True, category_id=id).order_by('-created_time')
	return render(request, 'blog/category.html', {'category': category, 'articles': articles})

def page_not_found(request):
	response = render_to_response('blog/404.html', {})
	response.status_code = 404
	return response

def page_error(request):
	response = render_to_response('blog/500.html', {})
	response.status_code = 404
	return response