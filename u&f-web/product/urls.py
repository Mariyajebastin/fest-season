from django.contrib import admin
from django.urls import path
from .views import index, submit
urlpatterns = [
    path('admin/', admin.site.urls),
	path('', index),
	path('submitData', submit)
]
