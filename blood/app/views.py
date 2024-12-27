from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
def login(req):
    if 'admin' in req.session:
        return redirect(admin_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        Username=req.POST['username']
        Password=req.POST['password']
        data=authenticate(username=Username,password=Password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['shop']=Username
                return redirect(admin_home)
            else:
                req.session['user']=Username
                return redirect(user_home)
        else:
            messages.warning(req, "invalid password")
            return redirect(login)
    else:
        return render(req,'login.html')
    

def admin_home(req):
    return render(req,'admin/home.html')

def user_home(req):
    return render(req,'user/home.html')

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req,"email alreadyin use")
            return redirect(register)
        return redirect(login)
    else:
        return render(req,'user/register.html')

