from django.shortcuts import render
from .models import recipe,ingredient,ingredientUsed
from .models import cuisines,dishtypes,mealtypes,marks
from django.db.models import Q,Case,IntegerField,Sum,When,F,Count
import datetime

# Create your views here.


def buildpantry(request):
    ingList=ingredient.objects.all()
    return render(request,'buildpantry.html',{'ingredients':ingList,'cuisines':cuisines,'dishtypes':dishtypes,'mealtypes':mealtypes,'marks':marks})

def getRecipe(request):
    queries={}
    filters=['cuisine','dishtype','mealtype','mark']
    hh=request.POST['hh']
    mm=request.POST['mm']
    

    for filter in filters:
        if len(request.POST.getlist(filter)) >0:
            queries[filter]=Q(**{filter+'__exact':request.POST.getlist(filter)[0]})
        else:
            queries[filter]=~Q(pk__in=[])
        for box in request.POST.getlist(filter)[1:]:
            queries[filter]|=Q(**{filter+'__exact':box})

    query=queries[filters[0]]
    for filter in filters[1:]:
        query&=queries[filter]

    time=False
    if(hh!='' or mm!=''):
        time=True

    if(hh!=''):
        hh=int(hh)
    else:
        hh=0
    
    if(mm!=''):
        mm=int(mm)
    else:
        mm=0
    
    if(time):
        timequery=Q(timetocook__lte=datetime.timedelta(hours=hh,minutes=mm))
    else:
        timequery=~Q(pk__in=[])
    
    query=query&timequery
    ingList=request.POST.getlist('ing')
    print(timequery)
    if len(ingList)>0:
        results=recipe.objects.filter(query,
                            ingredients__name__in=ingList).annotate(matches=Sum(
                                                                                Case(
                                                                                    When(ingredients__name__in=ingList, then=1),
                                                                                    output_field=IntegerField()
                                                                                    )
                                                                                ),
                                                                    total=Count('ingredients')).annotate(score=F('matches')/F('total')).order_by('-score')
    else:
        results=recipe.objects.filter(query)

    return render(request,'recipelist.html',{'result':results})

    

