from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, logout, authenticate
from example.models import Book, Comment
from django.core.mail import send_mail
from .forms import CommentForm

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

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = Comment.objects.filter(book=book)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.book = book
            comment.save()
            form = CommentForm()  # reset the form for a new comment
    else:
        form = CommentForm()

    context = {
        'book': book,
        'comments': comments,
        'form': form,
    }
    return render(request, 'book.html', context)


def conditions(request):
    return render(request, 'conditions.html')