from django.urls import path
from . import views

urlpatterns=[

    path('',views.userprofilepage,name='userprofilepage'),
    path('fav/',views.viewfavlist,name='viewfavlist'),
    path('history/',views.viewhistory,name='viewhistory'),
    path('removeFromSearch/',views.removeFromSearch,name='removeFromSearch')
]