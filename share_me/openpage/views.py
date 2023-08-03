from openpage.models import Passenger
def abc(request):
	if request.method=="POST":
		Passenger_name=request.POST.get("name")
	
