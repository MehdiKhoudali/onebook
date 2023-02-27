from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from example.models import Book

User = get_user_model()

def index(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('home')



def catalogue(request):
    book = Book.objects.all()
    context = {
        'books': book
    }
    return render(request, 'catalogue.html', context)