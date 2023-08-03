from django.db import models

# Create your models here.

class Product(models.Model):
	name=models.CharField(max_length=100)
	description=models.CharField(max_length=250)
	mrp=models.IntegerField(max_length=10)
	discount_in_precentage=models.IntegerField(max_length=10,null=True)
	created_date=models.DateField(auto_now=True,null=True)
	created_time=models.TimeField(auto_now=True,null=True)
	
	class Meta:
		db_table="product"
	def __str__(self):
		return self.name

class Customer(models.Model):
	nick_name=models.CharField(max_length=30)
	phone_number=models.IntegerField(max_length=10)
	email=models.EmailField(null=True)
	created_date=models.DateField(auto_now=True)
	created_time=models.TimeField(auto_now=True)
	
	class Meta:
		db_table="customer"
		
	def __str__(self):
		return self.nick_name
	
class Reimbursement(models.Model):
	types=models.CharField(max_length=100)
	Expense_date=models.DateField()
	description=models.TextField(max_length=250)
	amount=models.IntegerField()
	created_date=models.DateField(auto_now=True)
	created_time=models.TimeField(auto_now=True)
	
	class Meta:
		db_table="reimbursement"
		
	def __str__(self):
		return self.types
	
class MinutesOfMeeting(models.Model):
	Topic=models.TextField(max_length=100)
	conductor=models.CharField(max_length=20)
	conducted_date=models.DateField()
	conducted_time=models.CharField(max_length=10)
	present_persons=models.CharField(max_length=200)
	absent_persons=models.CharField(max_length=200)
	discussion=models.TextField(max_length=250)
	created_date=models.DateField(auto_now=True)
	created_time=models.TimeField(auto_now=True)
	
	class Meta:
		db_table="minutes_of_meeting"
	def __str__(self):
		return self.Topic
	

	
