from django.db import models

class Passenger(models.Model):
	name = models.CharField(max_length=250)
	addres=models.textField(max_length=250)