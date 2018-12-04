"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from chiters.views import ChitersList, ChitersDetail
from news.views import NewsList, NewsDetail


schema_view = get_schema_view(
    title='Chitcom API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

urlpatterns = [
    path('', include('home.urls')),
    path('docs/', schema_view, name='docs'),
    path('news/', include('news.urls')),
	path('paperchit/', include('paperchit.urls')),
    path('chiters/', include('chiters.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]


api_urlpatterns = [
    path('api/chiters/', ChitersList.as_view(), name='chiters_list'),
    path('api/chiters/<int:pk>/', ChitersDetail.as_view(), name='chiters_detail'),
    path('api/news/', NewsList.as_view(), name='news'),
    path('api/news/<int:pk>', NewsDetail.as_view(), name='news-detail'),
]

urlpatterns += api_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)