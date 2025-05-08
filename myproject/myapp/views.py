from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, "index.html", {"features": features})

# Create a view for the counter page
def counter(request):
    words = request.POST['words']
    word_count = len(words.split())
    context = {
        "words": words,
        'word_count': word_count,
    }
    return render(request, "counter.html", context)

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, "User created successfully")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, "register.html")
    

def Login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful")
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, "login.html")
    
def logout(request):
    auth_logout(request)
    return redirect("/")

def counter(request):
    posts = [1,2,3,4,5,"tim","tom","jerry"]
    return render(request,"counter.html", {"posts":posts})

def post(request, pk):
    return render(request, "post.html",{"pk":pk})