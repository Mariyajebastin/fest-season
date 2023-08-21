from django.contrib import admin
from django.urls import path
from .views import eyeCareIndex

urlpatterns = [
	path('admin/',admin.site.urls),
	path('eye-care',eyeCareIndex)

]