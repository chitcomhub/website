from django.urls import path
from .views import ArticleListView

app_name = 'paperchit'
urlpatterns = [
	path('', ArticleListView.as_view(), name='index'),
]