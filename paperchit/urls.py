from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
	ArticleListView,
	ArticleDetailView,
	ArticleCreateView
)


app_name = 'paperchit'
urlpatterns = [
	path('', ArticleListView.as_view(), name='index'),
	path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
	path('article/new/', ArticleCreateView.as_view(), name='article-create')
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)