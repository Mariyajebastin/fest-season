from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=250)
	age = models.IntegerField()
	address = models.CharField(max_length=250)
	
	class Meta:
		db_table = "student"
	
	def __str__(self):
		return self.name