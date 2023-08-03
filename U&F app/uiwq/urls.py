from django.contrib import admin
from django.urls import path, include

from uiwq.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
path('',dashboard)
]
