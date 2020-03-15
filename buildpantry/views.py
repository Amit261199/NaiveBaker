from django.shortcuts import render

# Create your views here.


def buildpantry(request):
    return render(request,'buildpantry.html')