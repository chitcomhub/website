from django.shortcuts import redirect, render
from .forms import PostForm

def chiters(request):
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