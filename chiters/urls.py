from django.urls import path

from . import views

app_name = 'chiters'
urlpatterns = [
	path('', views.chiters, name='chiters'),
	path('message/', views.message, name='message'),
]