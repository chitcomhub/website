from django.shortcuts import render
from .models import Article

def ArticleListView(ListView):
	model = Article
	template_name = 'paperchit/index.html'
	context_object_name = 'articles'
	ordering = ['-datetime']