from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
	model = Post
	template_name = 'news/index.html'

	def get_queryset(self):
		return Post.objects.order_by('-datetime')


class PostView(generic.DetailView):
	model = Post
	template_name = 'news/post.html'