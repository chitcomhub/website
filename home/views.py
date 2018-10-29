from django.shortcuts import render

def index(request):
	return render(request, 'home/index.html')

def works(request):
	return render(request, 'home/works.html')