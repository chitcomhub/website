from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):
	model = Article
	template_name = 'paperchit/index.html'
	context_object_name = 'articles'
	ordering = ['-datetime']


class ArticleDetailView(DetailView):
	model = Article