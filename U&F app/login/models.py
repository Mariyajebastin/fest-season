from django.db import models

# Create your models here.

class Festival(models.Model):
	name = models.CharField(max_length=250)
	date = models.DateField()
	about = models.TextField(max_length=250)
	
	
	class Meta:
		db_table = "festival"
		
	def __str__(self):
		return self.name