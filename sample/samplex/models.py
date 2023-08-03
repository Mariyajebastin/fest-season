from django.forms import models


class Candidate(models.Model):
	name=models.CharField(max_length=30)
	phone_number=models.IntegerField()
	address=models.CharField(max_length=100)
	
	class Meta:
		db_table= "candidate"
	
	def __str__(self):
		return self.name
	