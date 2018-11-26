from django.urls import path, include
from . import views

app_name = 'paperchit'
urlpatterns = [
	path('', views.index, name='index'),
]