from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.hashers import make_password,check_password
import requests
import random

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def service(request):
	return render(request,'service.html')

def contact(request):
	return render(request,'contact.html')

def appointment(request):
	return render(request,'appointment.html')

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				print("Password..........",make_password(request.POST['password']))
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=make_password(request.POST['password'])
					)
				msg="User Sign Up Successfuly"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Dose Note Matche"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			checkpassword=check_password(request.POST['password'],user.password)
			if checkpassword==True:
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,'index.html')
			else:
				msg="Password In Incorrect"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email Is Incorrect"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP For Forgot Password'
			message = "Hello "+user.fname+", Your OTP For Forgot Password Is "+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'otp':otp,'email':user.email})
		except:
			msg="Email Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})

	else:
		return render(request,'forgot-password.html')


def verify_otp(request):
	email=request.POST['email']
	otp=int(request.session['otp'])
	uotp=int(request.POST['uotp'])

	if otp==uotp:
		del request.session['otp']
		return render(request,'new-password.html')
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'msg':msg})

def new_password(request):
	if request.POST['new_password']==request.POST['cnew_password']:
		email=request.POST['email']
		user=User.objects.get(email=email)
		user.password=make_password(request.POST['new_password'])
		user.save()
		return redirect('logout')
	else:
		msg="New Password & Confirm New Password Dose Note Matched"
		return render(request,'new-password.html')


