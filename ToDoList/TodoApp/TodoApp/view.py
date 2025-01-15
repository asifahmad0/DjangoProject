from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .models import signup, TODOO

def Signup(request):

    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        passs = request.POST.get('pass')
        print(uname, email, passs)
        data = signup(Uname=uname,Email=email,Pass=passs)
        data.save()
        return redirect('/login')
    
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
      uname = request.POST.get('uname')
      passs = request.POST.get('pass')
      userr = authenticate(request,username=uname, password=passs )
      if userr is not None:
        #login(request, userr)
        return redirect('/todo')
      else:
        return redirect('/login')

    return render(request, 'login.html')

def todo(request):
    return render(request, 'index.html')