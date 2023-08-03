from django.contrib import admin
from django.urls import path, include
from .views import help

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', help)
]