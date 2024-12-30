from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def blood_login(request):
    if 'admin' in request.session:
        return redirect(admin_home)
    if 'user' in request.session:
        return redirect(user_home)
    if request.method=='POST':
        Username=request.POST['username']
        Password=request.POST['password']
        data=authenticate(username=Username,password=Password)
        if data:
            login(request,data)
            if data.is_superuser:
                request.session['admin']=Username
                return redirect(admin_home)
            else:
                request.session['user']=Username
                return redirect(user_home)
        else:
            messages.warning(request, "invalid password")
            return redirect(blood_login)
    else:
        return render(request,'login.html')


def blood_logout(req):
    logout(req)
    req.session.flush()
    return redirect(blood_login)



def admin_home(req):
    bloodrequest=BloodRequest.objects.all()
    return render(req,'admin/home.html',{'BloodRequest':bloodrequest})

def add_blood_request(req) :
    if 'admin' in req.session:
        if req.method=='POST':
            id=req.POST['id']
            patient_name=req.POST['pname']
            description=req.POST['descrip']
            place=req.POST['place']
            contact_no=req.POST['cno']
            request_date=req.POST['reqdate']
            data=BloodRequest.objects.create(id=id, patient_name=patient_name, description=description, place=place,contact_no=contact_no,request_date=request_date)
            data.save()
            return redirect(admin_home)
        else:
            
            return render(req,'admin/addbloodrequest.html')
    else:
        return redirect(blood_login) 




def user_home(req):
    if 'user' in req.session:
        bloodrequest=BloodRequest.objects.all()
        return render(req,'user/home.html',{'BloodRequest':bloodrequest})
    else:
        return redirect(blood_login)
    

def Register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        password=req.POST['password']
        
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req,"username already exist")
            return redirect(Register)
        return redirect(blood_login)
    else:
        return render(req,'user/register.html')
    

def about_us(req):
    return render(req,'user/about.html')

def view_patient(req,pid):
       bloodrequest=BloodRequest.objects.get(pk=pid)
       return render(req,'user/view_pro.html',{'BloodRequest': bloodrequest})



    
