from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import signup, TODOO

def Signup(request):

    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        passs = request.POST.get('pass')
        print(uname, email, passs)
        data = User.objects.create_user(uname,email,passs)
        data = signup(Uname=uname,Email=email,Pass=passs)
        data.save()
        return redirect('/login')
    
    return render(request, 'signup.html')

def Login(request):
    if request.method == 'POST':
      uname = request.POST.get('uname')
      passs = request.POST.get('pass')
      userr = authenticate(request,username=uname, password=passs )
      print(userr)
      if userr is not None:
        login(request, userr)
        return redirect('/todo',{'uname':uname})
      else:
        print(userr, request.method)
        return redirect('/login')

    return render(request, 'login.html')

def todo(request):
    if request.method == 'POST':
       Todo=request.POST.get('Todo')
       print(Todo)
       data = TODOO(title=Todo,user= request.user)
       data.save()
    todoo=TODOO.objects.filter(user=request.user).order_by('-date')
    user=request.user
    return render(request, 'index.html', {'todoo':todoo})

def edit_todo(request):
   return

def delet_todo(request,srno):
   obj=TODOO.objects.get(srno=srno)
   obj.delete()
   return redirect('/todo')

def signout(request):
   logout(request)
   return redirect('/login')
