from django.shortcuts import render

from .models import Post

def index(request):
	post_list = Post.objects.order_by('-datetime')
	return render(request, 'news/index.html', {'post_list': post_list})