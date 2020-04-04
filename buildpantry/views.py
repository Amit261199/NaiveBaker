from django.shortcuts import render
from .models import recipe,ingredient,ingredientUsed
from .models import cuisines,dishtypes,mealtypes,marks
# Create your views here.


def buildpantry(request):
    ingList=ingredient.objects.all()
    return render(request,'buildpantry.html',{'ingredients':ingList})

def getRecipe(request):
    cuisineList=[]
    for entry in cuisines:
        cuisineList.append(entry[0])
    mealList=[]
    for entry in mealtypes:
        mealList.append(entry[0].replace(' ','-'))
    dishList=[]
    for entry in dishtypes:
        dishList.append(entry[0].replace(' ','-'))
    markList=[]
    for entry in marks:
        markList.append(entry[0])
        
       
        print(request.POST.getlist('ing'))
        
        return render(request,'buildpantry.html')

    

