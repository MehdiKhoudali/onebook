# example/urls.py
from example.views import index
from django.urls import path, include

urlpatterns = [
    path('', index, name="home"),
]