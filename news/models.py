from django.db import models


class Post(models.Model):
	title = models.CharField('Заголовок', max_length=200)
	context = models.TextField('Описание')
	datetime = models.DateTimeField('Дата публикации')
	pic = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение', help_text='Ширина изображения должна быть 800px')

	def __str__(self):
		return self.title