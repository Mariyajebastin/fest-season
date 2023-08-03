from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sale_home.models import Product, Customer, Reimbursement, MinutesOfMeeting
from sale_home.serializer import ProductSerializer, PSerializer, CustomerSerializer, CSerializer, \
	ReimbursementSerializer, RSerializer, MOMSerializer, Mserializer


# Create your views here.

@api_view(["GET","POST","PUT","DELETE"])
def product(request):
	if request.method=="GET":
		id=PSerializer(data=request.data)
		if id.is_valid():
			id=request.data.get("id")
			if Product.objects.filter(id=id).exists():
				product=Product.objects.get(id=id)
				products=ProductSerializer(product)
				return JsonResponse(products.data,safe=False)
			else:
				return JsonResponse({
					"messsage":"product not presented in database"
				})
		product_details=Product.objects.all()
		if len(product_details)>0:
			product=ProductSerializer(product_details,many=True)
			print(product.data)
			return JsonResponse(product.data, safe=False)
		return JsonResponse({
			"message":"There is no data"
		})
	if request.method=="POST":
		product_data=ProductSerializer(data=request.data)
		if product_data.is_valid():
			product_data.save()
			return JsonResponse({
				"message":"Data received successfully"
			})
		return Response(product_data.errors)
	if request.method=="DELETE":
		id=PSerializer(data=request.data)
		if id.is_valid():
			id=request.data.get("id")
			if Product.objects.filter(id=id).exists():
				product=Product.objects.filter(id=id)
				product.delete()
				return JsonResponse({
					"message":"id deleted successfully"
				})
			else:
				return JsonResponse({
					"message":"id not presented in database"
				})
		product=Product.objects.all()
		product.delete()
		return JsonResponse({
			"message":"Data deleted successfully"
		})
@api_view(["GET","POST","PUT","DELETE"])
def customer(request):
	if request.method=="GET":
		id=CSerializer(data=request.data)
		if id.is_valid():
			id=request.data.get("id")
			if Customer.objects.filter(id=id).exists():
				id=Customer.objects.get(id=id)
				ids=CustomerSerializer(id)
				return JsonResponse(ids.data,safe=False)
			
			else:
				return JsonResponse({
					"message":"Customer is not presented in database"
				})
		customer_details=Customer.objects.all()
		if len(customer_details)>0:
			customer=CustomerSerializer(customer_details,many=True)
			print(customer.data)
			return JsonResponse(customer.data,safe=False)
		return JsonResponse({
				"message":"There is no data"
			})
	if request.method=="POST":
		customer_data=CustomerSerializer(data=request.data)
		if customer_data.is_valid():
			customer_data.save()
			return JsonResponse({
				"message":"Data received successfully"
			})
		return Response(customer_data.errors)
	if request.method=="DELETE":
		id=CSerializer(data=request.data)
		if id.is_valid():
			id=request.data.get("id")
			if Customer.objects.filter(id=id).exists():
				customer=Customer.objects.filter(id=id)
				customer.delete()
				return JsonResponse({
					"message":"Id is deleted successfully"
				})
			else:
				return JsonResponse({
					"message":"Id is not presented in database"
				})
		customer=Customer.objects.all()
		customer.delete()
		return JsonResponse({
			"message":"Data deleted successfully"
		})

@api_view(["GET","POST","PUT","DELETE"])
def reimbursement(request):
	if request.method=="GET":
		id=RSerializer(data=request.data)
		if id.is_valid():
			id=request.data.get("id")
			if Reimbursement.objects.filter(id=id).exists():
				id=Reimbursement.objects.get(id=id)
				ids=ReimbursementSerializer(id)
				return JsonResponse(ids.data,safe=False)
			else:
				return JsonResponse({
					"message":"id is not presented in database"
				})
		reimbursement_details=Reimbursement.objects.all()
		if len(reimbursement_details)>0:
			reimbursement=ReimbursementSerializer(reimbursement_details,many=True)
			print(reimbursement.data)
			return JsonResponse(reimbursement.data,safe=False)
		return JsonResponse({
			"message":"There is no data"
		})
	if request.method=="POST":
		reimbursement_data=ReimbursementSerializer(data=request.data)
		if reimbursement_data.is_valid():
			reimbursement_data.save()
			return JsonResponse({
				"message":"Data received successfully"
			})
		return Response(reimbursement_data.errors)
	if request.method=="DELETE":
		id=RSerializer(data=request.data)
		if id.is_valid():
			id=request.data.get("id")
			if Reimbursement.objects.filter(id=id).exists():
				reimbursement=Reimbursement.objects.filter(id=id)
				reimbursement.delete()
				return JsonResponse({
					"message":"Data deleted successfully"
				})
			else:
				return JsonResponse({
					"message":"Id is not presented in database"
				})
		reimbursement=Reimbursement.objects.all()
		reimbursement.delete()
		return JsonResponse({
			"message":"Data deleted successfully"
		})

@api_view(["GET","POST","PUT","DELETE"])
def mom(request):
	if request.method=="GET":
		id=Mserializer(data=request.data)
		if id.is_valid():
			id=request.data.get("id")
			if MinutesOfMeeting.objects.filter(id=id).exists():
				id=MinutesOfMeeting.objects.get(id=id)
				ids=MOMSerializer(id)
				return JsonResponse(ids.data,safe=False)
			else:
				return JsonResponse({
					"message":"Id is not presented in database"
				})
		mom_details=MinutesOfMeeting.objects.all()
		if len(mom_details)>0:
			mom=MOMSerializer(mom_details,many=True)
			print(mom.data)
			return JsonResponse(mom.data,safe=False)
		return JsonResponse({
			"message":"There is no data"
		})
	if request.method=="POST":
		mom_data=MOMSerializer(data=request.data)
		if mom_data.is_valid():
			mom_data.save()
			return JsonResponse({
				"message":"Data received successfully"
			})
		return Response(mom_data.errors)
	if request.method=="DELETE":
		id = Mserializer(data=request.data)
		if id.is_valid():
			id = request.data.get("id")
			if MinutesOfMeeting.objects.filter(id=id).exists():
				mom=MinutesOfMeeting.objects.filter(id=id)
				mom.delete()
				return JsonResponse({
					"message":"Id deleted successfully"
				})
			else:
				return JsonResponse({
					"message":"Id in not presented in database"
				})
		
		mom=MinutesOfMeeting.objects.all()
		mom.delete()
		return JsonResponse({
			"message":"Data deleted successfully"
		})
		
	
		