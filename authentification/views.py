from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book
from django.urls import reverse_lazy
from django.http import HttpResponse



def signup(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		my_user = User.objects.create_user(username, password, email)
		my_user.save()
		return redirect('home')
	return render(request, 'signup.html')

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password, is_staff=False)
		if user is not None:
			login(request,user)
			return redirect('home')
	return render(request, 'login.html')

@login_required(login_url="/login/")
def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login/')
def userPage(request, id=User.id):
	return render(request, 'userPage.html')

@login_required(login_url="/login/")
def catalogue(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'catalogue.html', context=context)
