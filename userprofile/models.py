from django.db import models
from django.contrib.auth.models import User
from django import forms
from buildpantry.models import recipe
from django.utils.safestring import mark_safe

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    dateofbirth=models.DateField(auto_now=False,auto_now_add=False)
    profilepicture=models.ImageField(upload_to='pics',default='pics/avatar.jpg')
    favourites=models.ManyToManyField(recipe,related_name='favouriteof')
    searchhistory=models.ManyToManyField(recipe,related_name='searchedby')

    def image(self):
        return mark_safe('<img src="%s" style="width: 150px; height=160px;" />' % self.profilepicture.url)
