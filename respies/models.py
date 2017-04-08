from django.db import models

class Recipie(models.Model):
	recipie_name = models.CharField(max_length=200)
	ingrediants = models.CharField(max_length=500)
	process = models.TextField(max_length=1000)
	
	def __str__(self):
		return self.recipie_name

	class Meta:
		verbose_name='Recipesssssssssssss'
		verbose_name_plural='Mani'

