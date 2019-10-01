from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	opening_time = models.CharField(max_length=100)
	closing_time = models.CharField(max_length=100)


	def __str__(self):
		return self.name
