from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)

app_name = 'news'
urlpatterns = [
	path('', PostListView.as_view(), name='index'),
	path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)