from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:post_id>/', views.post, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)