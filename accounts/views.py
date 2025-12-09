from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import ContactMessage 


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name  = request.POST.get('last_name', '')
        username   = request.POST.get('username', '')
        email      = request.POST.get('email', '')
        password1  = request.POST.get('password1', '')
        password2  = request.POST.get('password2', '')


        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'Username Taken')
               return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name = first_name,)
                user.save()
                messages.success(request, "User created successfully!")
                return redirect('login')

        else:
           messages.info(request,"password not matching")
           return redirect('register')

    return render(request,'register.html')

def logout_view(request):
    logout(request)
    return redirect('/')
    
