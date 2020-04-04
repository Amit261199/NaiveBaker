from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def userprofilepage(request):
    return render(request,'userprofilepage.html')

def signup_view(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST )
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect('buildpantry:getRecipe')
	else:
		form = UserCreationForm()
	context = {
		'form' : form
	}
	return render(request,'user_create.html',context)

def login_view(request):
	if request.method=='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			return redirect('buildpantry:getRecipe')
	else:
		form = AuthenticationForm()
	context = {
		'form' : form
	}
	return render(request,'login.html',context)

