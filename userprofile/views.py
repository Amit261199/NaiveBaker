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
		if int(request.POST['age'])<=15:
			messages.info(request,'age is below minimum age')
			return redirect('../signup')
		if request.POST['psw']!=request.POST['psw-repeat']:
			messages.info(request,'passwords do not match')
			return redirect('../signup')
		if User.objects.filter(username__exact=request.POST['uname']).exists():
			messages.info(request,'username already taken')
			return redirect('../signup')
		try:
			with transaction.atomic():
				u=User.objects.create_user(username=request.POST['uname'],email=request.POST['email'],password=request.POST['psw'],is_staff=False)
				p=profile(user=u,age=request.POST['age'])
				p.save()
				return redirect('../login')
		except IntegrityError:
			messages.info(request,'Some error occurred. signup failed. please try again')
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
			login(request,user)
			return redirect('../userprofile')
		else:
			messages.info(request,'Your username and password is incorrect. Please try again.')
			return redirect('../login')
	else:
		if request.user.is_authenticated:
			return redirect('../userprofile')
		else:
			form=AuthenticationForm()
			return render(request,'login.html',{'form':form})