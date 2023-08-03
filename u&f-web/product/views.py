from django.http import HttpResponse
from django.shortcuts import render

from product.models import Student


# Create your views here.


def index(request):
	return render(request,"index.html")


def submit(request):
	Student.objects.all().delete()
	if request.method=="POST":
		address = request.POST.get('address')
		age = request.POST.get('age')
		name = request.POST.get('name')
		student = Student(address=address,age=age,name=name)
		student.save()
		for x in Student.objects.all():
			print(x.name,x.address,x.age)
	return HttpResponse("data is submitted")

