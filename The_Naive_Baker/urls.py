"""The_Naive_Baker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from userprofile.views import home,login_view,contactpage,logoutfromsite,signup_view
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('', home),
    path('admin/', admin.site.urls),
    path('userprofile/', include('userprofile.urls')),
    path('buildpantry/', include('buildpantry.urls')),
    path('login/', login_view,name='login'),
    path('signup/', signup_view,name='signup'),
    path('logout/', logoutfromsite,name='logoutfromsite'),
    path('recipes/',include('buildpantry.urls')),
    path('contact/',contactpage,name='contactpage'),
    
]

urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)