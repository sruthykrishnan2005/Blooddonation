from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from .forms import *
import os
import random
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
# from .models import Donor
# from .forms import DonorRegistrationForm
# from .forms import BloodDonationRequestForm




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
    

def edit_patient(req,pid):
    if req.method=='POST':
        id=req.POST['id']
        patient_name=req.POST['pname']
        description=req.POST['descrip']
        place=req.POST['place']
        contact_no=req.POST['cno']
        request_date=req.POST['reqdate']
        BloodRequest.objects.filter(pk=pid).update(id=id, patient_name=patient_name, description=description, place=place,contact_no=contact_no,request_date=request_date)
        data=BloodRequest.objects.get(pk=pid)
        data.save()
        return redirect(admin_home)
    else:
        data=BloodRequest.objects.get(pk=pid)
        return render(req,'admin/edit.html',{'data':data})
    

def delete_patient(req,pid):
    data=BloodRequest.objects.get(pk=pid)
    data.delete()
    return redirect(admin_home)


def view_register_donate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        blood_group = request.POST.get('bldgrp')
        contact_number = request.POST.get('cno')
        city = request.POST.get('city')
        age = request.POST.get('age')
        
        if name and blood_group and contact_number and city and age:
            data = Donor(name=name,blood_group=blood_group,contact_number=contact_number,city=city,age=age)
            data.save()
            return redirect('admin_home')

    donors = Donor.objects.all()
    return render(request, 'admin/viewregisterdonate.html', {'donors': donors})


def view_request_blood(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        place = request.POST.get('place')
        blood_type = request.POST.get('blood_type')
        message = request.POST.get('message')
        
        if name and phone and place and blood_type and message:
            data = BloodDonationRequest(name=name,phone=phone,place=place,blood_type=blood_type,message=message)
            data.save()
            return redirect('admin_home')

    requests = BloodDonationRequest.objects.all()
    return render(request, 'admin/viewrequestblood.html', {'requests': requests})






    
def user_home(req):
    if 'user' in req.session:
        bloodrequest=BloodRequest.objects.all()
        return render(req,'user/home.html',{'BloodRequest':bloodrequest})
    else:
        return redirect(blood_login)


def blood_donation_request(request):
    print('jgyhfyfy')
    blood_types = [
        "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"
    ]
    if request.method =='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        place = request.POST.get('place')
        blood_type = request.POST.get("blood_type")
        message = request.POST.get('message')

        if name and phone and place and blood_types and message:
            data = BloodDonationRequest(name=name, phone=phone, place=place,blood_type=blood_type, message=message)
            data.save()
            print(f"Name: {name}, Phone: {phone}, Place: {place}, Blood type: {blood_types}, Message: {message}") 
            return redirect(user_home)


def view_request_blood_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        place = request.POST.get('place')
        blood_type = request.POST.get('blood_type')
        message = request.POST.get('message')

       
        if name and phone and place and blood_type and message:
            data = BloodDonationRequest(name=name,phone=phone,place=place,blood_type=blood_type,message=message)
            data.save()
            
            return redirect('user_home')

    requests = BloodDonationRequest.objects.all()
    active=BloodDonationRequest.objects.filter(is_active=True)
    return render(request, 'user/viewrequestblooduser.html', {'requests': requests, 'active':active})

def qty_in(request,pk):
    data=BloodDonationRequest.objects.get(pk=pk)
    data.is_active=False
    data.save()
    print(data.is_active)
    return redirect(view_request_blood_user)


def generate_otp():
    return str(random.randint(100000, 999999))

def verify_otp(request):
    Username = request.session.get('username')
    stored_otp = request.session.get('otp')

 
    if not Username or not stored_otp:
        messages.error(request, "Session expired. Please log in again.")
        return redirect('blood_login')

    if request.method == "POST":
        if "resend_otp" in request.POST:
            try:
                user = User.objects.get(username=Username)
                new_otp = generate_otp()
                request.session['otp'] = new_otp  

                send_mail(
                    'Your New OTP',
                    f'Your new OTP is {new_otp}. Please enter it to verify your login.',
                    'your_email@example.com', 
                    [user.email],
                    fail_silently=False,
                )

                messages.success(request, "A new OTP has been sent to your email.")
                return redirect('verify_otp')

            except User.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect('blood_login')
            
        entered_otp = request.POST.get('otp', '')

        if entered_otp == stored_otp:
            try:
                user = User.objects.get(username=Username)

                if user.is_superuser:
                    messages.error(request, "Admins do not require OTP verification.")
                    return redirect('blood_login')

                login(request, user) 

                del request.session['otp']
                request.session['user'] = Username  

                return redirect('user_home') 

            except User.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect('blood_login')

        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('verify_otp')

    return render(request, 'user/otpview.html')


def Register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']

        try:
            data = User.objects.create_user(first_name=uname,username=uname, email=email, password=password, )
            data.save()
            
            otp = generate_otp()
            request.session['otp'] = otp
            request.session['username'] = uname

            send_mail(
                'Your OTP for Login',
                f'Your OTP is {otp}. Please enter it to complete your registration.',
                'your_email@example.com',  
                [email],  
                fail_silently=False,
            )

            
            return redirect('verify_otp')

        except Exception as e:
            messages.warning(request, "Username already exists ")
            return redirect('register') 

    else:
        return render(request, 'user/register.html')

def about_us(req):
    return render(req,'user/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        message = request.POST.get('message')

    
        if not name or not email or not phone or not city or not message:
            messages.error(request, "All fields are required.")
        else:
            try:
              
                data = Contact.objects.create(
                    name=name, 
                    email=email, 
                    phone=phone, 
                    city=city, 
                    message=message
                )
                data.save()
                
                messages.success(request, "Your message has been sent successfully!")

                return redirect('contact') 

            except Exception as e:
                messages.error(request, "There was an error processing your message. Please try again.")
                return redirect('contact')  

   
    return render(request, 'user/contact.html')

def view_patient(request,pid):
    if request.method == 'POST':
        name = request.POST.get('name')
        blood_group = request.POST.get('bldgrp')
        contact_number = request.POST.get('cno')
        city = request.POST.get('city')
        age = request.POST.get('age')
        
        data = Donor(name=name,blood_group=blood_group,contact_number=contact_number,city=city,age=age)
        data.save()

        return redirect(register_to_donate)
    # donors = Donor.objects.all()
    # return render(request, 'user/registertodonate.html', {'register_to_donate': donors})
    data=BloodRequest.objects.get(pk=pid)
    return render(request,'user/viewpatient.html',{'BloodRequest': data})

def contact(req):
    return render(req,'user/contact.html')


def register_to_donate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        blood_group = request.POST.get('bldgrp')
        contact_number = request.POST.get('cno')
        city = request.POST.get('city')
        age = request.POST.get('age')
        
        data = Donor(name=name,blood_group=blood_group,contact_number=contact_number,city=city,age=age)
        data.save()

        return redirect(register_to_donate)

    donors = Donor.objects.all()

    return render(request, 'user/registertodonate.html', {'register_to_donate': donors})








# def blood_donation_request(request):
#     if request.method == "POST":
#         form = BloodDonationRequestForm(request.POST)
#         if form.is_valid():
#             # Save the data to the database
#             blood_request = BloodDonationRequest(
#                 full_name=form.cleaned_data['full_name'],
#                 email=form.cleaned_data['email'],
#                 phone=form.cleaned_data['phone'],
#                 message=form.cleaned_data['message']
#             )
#             blood_request.save()
#             return HttpResponse("Thank you for your blood donation request! We will get in touch with you soon.")
#     else:
#         form = BloodDonationRequestForm()

#     return render(request, 'user/home.html', {'form': form})



# def view_patient(request, pid):
  
#     try:
#         patient = BloodRequest.objects.get(id=pid)
#     except BloodRequest.DoesNotExist:
#         return HttpResponse("Patient not found", status=404)

#     if request.method == "POST":
#         form = DonorRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('') 

#     else:
#         # Display empty form
#         form = DonorRegistrationForm()

#     # Render the patient details page with the form
#     return render(request, 'user/viewpatient.html', {'patient': patient, 'form': form})


# def view_patient(req,pid):
#     if 'admin' in req.session:
#         data=Donor.objects.all(pk=pid)
#         return render(req,'user/viewpatient.html',{'donors':data})
#     else:
#         return redirect(register_to_donate)
