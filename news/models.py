from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField('Заголовок', max_length=200)
	content = models.TextField('Описание')
	datetime = models.DateTimeField('Дата публикации', default=timezone.now)
	pic = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение', help_text='Ширина и высота 800x400px')
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('news:post-detail', kwargs={'pk': self.pk})