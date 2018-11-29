from django.urls import path

from . import views

app_name = 'chiters'
urlpatterns = [
	path('', views.chiters, name='chiters'),
	path('register/', views.register, name='register'),
	path('message/', views.message, name='message'),
	path('chiters/', views.ChitersList.as_view(), name='chiters_list'),
	path('chiters/<int:pk>/', views.ChitersDetail.as_view(), name='chiters_detail')
]