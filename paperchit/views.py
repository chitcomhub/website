from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView
)
from .models import Article


class ArticleListView(ListView):
	model = Article
	template_name = 'paperchit/index.html'
	context_object_name = 'articles'
	ordering = ['-datetime']


class ArticleDetailView(DetailView):
	model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Article
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)