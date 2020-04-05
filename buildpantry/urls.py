from django.urls import path
from . import views

urlpatterns=[

    path('',views.buildpantry,name='buildpantry'),
    path('getrecipe',views.getRecipe,name="getRecipe"),
    path('display/<recipe_title>/',views.displayRecipe,name="displayRecipe"),
    path('getallrecipe',views.recipes_all,name="recipes_all")
]