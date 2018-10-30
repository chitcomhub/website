from django.shortcuts import redirect, render
from .forms import PostForm

from .models import Chiter

def chiters(request):
	chiter_list = Chiter.objects.order_by('-date')
	context = {'chiter_list': chiter_list}
	return render(request, 'chiters/chiters.html', context)

def register(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()
			post.save()
			return redirect('/chiters/message')
	else:
		form = PostForm()
	return render(request, 'chiters/register.html', {'form': form})

def message(request):
	return render(request, 'chiters/message.html')