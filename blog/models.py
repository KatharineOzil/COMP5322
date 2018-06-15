# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# Create your models here.

class Category(models.Model):
	category = models.CharField(max_length=20)
	cover = models.ImageField(upload_to='static/category_cover/', blank=False, default='static/category_cover/default.png')

	def __str__(self):
		return self.category

class Article(models.Model):
	cover = models.ImageField(upload_to='static/cover/', blank=False)
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	content = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_time = models.DateTimeField(default=timezone.now)
	visible = models.BooleanField(default=True)
	attachment = models.FileField(upload_to="static/attachment/", blank=True)

	def __str__(self):
		return self.title

class Comment(MPTTModel):
	content = models.CharField(max_length=2000)
	author = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	created_time = models.DateTimeField(default=timezone.now)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
            on_delete=models.CASCADE)
	status = models.BooleanField(default=True)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)

	def __str__(self):
		return self.content 

	class MPTTMeta:
		order_insertion_by = ['-created_time']
		tree_manager_name = 'objects'

class User(AbstractUser):
    intro = models.TextField(blank=True, default='-')

