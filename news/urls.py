from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.PostView.as_view(), name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)