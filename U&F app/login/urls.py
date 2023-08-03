from django.contrib import admin
from django.urls import path

from login.views import xyz, delete, view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("/xyz", xyz),
    path("/delete", delete),
    path('/view', view)
    
]