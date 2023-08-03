from django.http import HttpResponse
from django.shortcuts import render

from login.models import Festival


# Create your views here.


def xyz(request):
	if request.method == "POST":
		festival_name = request.POST.get('festival_name')
		festival_date = request.POST.get("festival_date")
		festival_about = request.POST.get("about_festival")
		for x in range(1,10):
			festival = Festival(name=festival_name,date = festival_date, about = festival_about)
			festival.save()
	return render(request,"login page.html")


def delete(request):
	if Festival.objects.count() > 0:
		Festival.objects.all().delete()
		return HttpResponse("data deleted")
	return HttpResponse("no data found")

def view(request):
	if Festival.objects.count() > 0:
		for x in Festival.objects.all():
			print(x.name)
		return HttpResponse("data retrived")
	return HttpResponse("no data found")
	