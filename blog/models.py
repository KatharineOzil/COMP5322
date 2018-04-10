# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Category(models.Model):
	category = models.CharField(max_length=20)

	def __str__(self):
		return self.category

class Article(models.Model):
	cover = models.ImageField(upload_to='blog/static/cover/', blank=False)
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	content = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_time = models.DateTimeField(default=timezone.now)
	visible = models.BooleanField(default=True)
	attachment = models.FileField(upload_to="blog/static/attachment/", blank=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	content = models.CharField(max_length=2000)
	author = models.CharField(max_length=100)
	created_time = models.DateTimeField(default=timezone.now)
	status = models.BooleanField(default=False)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)

	def __str__(self):
		return self.author

class User(AbstractUser):
    intro = models.TextField(blank=True, default='-')

class feedback(models.Model):
	from_id = models.ForeignKey(User, on_delete=models.CASCADE)
	to_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
	content = models.CharField(max_length=2000)
	created_time = models.DateTimeField(default=timezone.now)