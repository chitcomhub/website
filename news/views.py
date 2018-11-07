from django.shortcuts import get_object_or_404, render

from .models import Post

def index(request):
	post_list = Post.objects.order_by('-datetime')
	return render(request, 'news/index.html', {'post_list': post_list})

def post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'news/post.html', {'post': post})