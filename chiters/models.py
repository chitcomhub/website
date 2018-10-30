from django.db import models


class Chiter(models.Model):
	name = models.CharField(max_length = 200)
	nickname = models.CharField(max_length = 200)
	direction = models.CharField(max_length = 200)
	technology = models.CharField(max_length = 400)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name