from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import transaction, IntegrityError
from .models import profile
from django.contrib.auth.models import User
import datetime
import os
from django.conf import settings

# Create your views here.


def home(request):
	return render(request,'home.html')

def userprofilepage(request):
	if not request.user.is_authenticated:
		messages.info(request,'Permission Denied. You need to Log in first')
		return redirect(reverse('login'))
	return render(request,'userprofilepage.html')
		
def contactpage(request):
	return render(request,'contact.html')

def logoutfromsite(request):
	logout(request)
	messages.info(request,'Logged out successfully')
	return redirect('../')

@transaction.atomic
def signup_view(request):
	if request.method=='POST':
		dob=datetime.date(int(request.POST['dob'].split('/')[2]),int(request.POST['dob'].split('/')[1]),int(request.POST['dob'].split('/')[0]))
		today=datetime.date.today()
		expected=datetime.date(int(request.POST['dob'].split('/')[2])+15,int(request.POST['dob'].split('/')[1]),int(request.POST['dob'].split('/')[0]))
		if today<expected:
			messages.info(request,'Your age is below minimum age. You must be aged atleast 15 years to continue.')
			return redirect('../signup')
		if request.POST['psw']!=request.POST['psw-repeat']:
			messages.info(request,'Your passwords do not match. Please enter them correctly.')
			return redirect('../signup')
		if User.objects.filter(username__exact=request.POST['uname']).exists():
			messages.info(request,'This username already taken. Please try another one.')
			return redirect('../signup')
		try:
			with transaction.atomic():
				u=User.objects.create_user(username=request.POST['uname'],email=request.POST['email'],password=request.POST['psw'],is_staff=False)
				if 'profilepicture' in request.FILES.keys():
					imgname=request.POST['uname']+'_'+request.FILES['profilepicture'].name
					picturepath=os.path.join('pics/',imgname)
					path=os.path.join(settings.MEDIA_ROOT,picturepath)
					fout=open(path,'wb+')
					for chunk in request.FILES['profilepicture'].chunks():
						fout.write(chunk)
					fout.close()
					p=profile(user=u,dateofbirth=dob,profilepicture=picturepath)
					p.save()
				else:
					p=profile(user=u,dateofbirth=dob)
					p.save()
				return redirect('../login')
		except IntegrityError:
			messages.info(request,'Server error occurred. signup failed. please try again')
			return redirect('../signup')
	else:
		if request.user.is_authenticated:
			return redirect('../userprofile')
		else:
			return render(request,'signup.html')
		

def login_view(request):
	if request.method=='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			if user.is_staff:
				messages.info(request,'You are not permitted to access this page. Please login through the admin page.')
				return redirect('../login')
			else:
				login(request,user)
				return redirect('../userprofile')
		else:
			messages.info(request,'Your username and/or password is incorrect. Please try again.')
			return redirect('../login')
	else:
		if request.user.is_authenticated:
			return redirect('../userprofile')
		else:
			form=AuthenticationForm()
			return render(request,'login.html',{'form':form})