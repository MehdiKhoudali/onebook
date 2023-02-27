# example/urls.py
from example.views import index, signup, logoutPage, loginPage, catalogue
from django.urls import path, include

urlpatterns = [
    path('', index, name="home"),
    path('signup/', signup, name="signup"),
    path('logout/', logoutPage, name="logout"),
    path('login/', loginPage, name="login"),
    path('catalogue/', catalogue, name="catalogue")
]