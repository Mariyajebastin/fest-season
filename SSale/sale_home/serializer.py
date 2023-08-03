from rest_framework import serializers

from sale_home.models import Product, Customer, Reimbursement, MinutesOfMeeting


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model=Product
		exclude=["created_date","created_time"]

class PSerializer(serializers.Serializer):
	id=serializers.CharField(max_length=5)
	
class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Customer
		exclude=["created_date","created_time"]
		
class CSerializer(serializers.Serializer):
	id=serializers.CharField(max_length=5)

class ReimbursementSerializer(serializers.ModelSerializer):
	class Meta:
		model=Reimbursement
		exclude=["created_date","created_time"]
class RSerializer(serializers.Serializer):
	id=serializers.CharField(max_length=5)

class MOMSerializer(serializers.ModelSerializer):
	class Meta:
		model= MinutesOfMeeting
		exclude=["created_date","created_time"]
class Mserializer(serializers.Serializer):
	id=serializers.CharField(max_length=5)