from django.contrib import admin
from django.urls import path, include
from .views import catalogue, signup, loginPage, logoutPage


urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),
    path('catalogue/', catalogue, name="catalogue")
]