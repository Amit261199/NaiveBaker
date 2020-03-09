from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def userprofilepage(request):
    return render(request,'User_Profile_page.html')