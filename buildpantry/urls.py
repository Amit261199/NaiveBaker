from django.urls import path
from . import views

urlpatterns=[

    path('',views.buildpantry,name='buildpantry'),
    path('getrecipe',views.getRecipe,name="getRecipe")
]