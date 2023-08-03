from django.contrib import admin
from django.urls import path
from openpage.views import abc
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/a',abc)

	]