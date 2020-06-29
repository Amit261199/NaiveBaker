from django.db import models
from django.contrib.auth.models import User
from django import forms
from buildpantry.models import recipe
from django.utils.safestring import mark_safe
import os
# Create your models here.

def get_file_path(instance, filename):
    return os.path.join('pics', str(instance.user.id)+'_'+filename)

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    dateofbirth=models.DateField(auto_now=False,auto_now_add=False)
    profilepicture=models.ImageField(upload_to=get_file_path,default='pics/avatar.jpg')
    favourites=models.ManyToManyField(recipe,related_name='favouriteof')
    searchhistory=models.ManyToManyField(
        recipe,
        through='history',
        through_fields=('userprofile','recipe_searched'))
    def image(self):
        return mark_safe('<img src="%s" style="width: 150px; height=160px;" />' % self.profilepicture.url)



class history(models.Model):
    number=models.BigAutoField(primary_key=True)
    userprofile=models.ForeignKey(profile,on_delete=models.CASCADE)
    recipe_searched=models.ForeignKey(recipe,on_delete=models.CASCADE)
    timestamp=models.TimeField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userprofile', 'recipe_searched','timestamp'], name='unique_history')
        ]
