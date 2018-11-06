from django.db import models


class Post(models.Model):
	title = models.CharField('Заголовок', max_length=200)
	context = models.TextField('Описание')
	datetime = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.title