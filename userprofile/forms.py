from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import profile

# class UserProfileForm(UserCreationForm):
#     profilepicture = forms.ImageField(required=True)
#     age = forms.IntegerField(required=True)
#     email=forms.EmailField(required=True)
#     password1 = forms.CharField(required=True,widget=forms.PasswordInput())
#     password1 = forms.CharField(required=True,widget=forms.PasswordInput())


#     def clean(self):
#         form_data=self.cleaned_data
#         username=form_data['username']
#         if User.objects.filter(username=form_data['username']).exists():
#             raise forms.ValidationError(u'Username "%s" is already in use.' % username)
#         if form_data['age'] < 15:
#             raise forms.ValidationError("Users of age below 15 years are not allowed", code="age",)
#         if form_data['password1']==form_data['password2']:
#             raise forms.ValidationError("Both the passwords must match",code="password")
        
#         return form_data

#     def save(self, commit=True):
#         if not commit:
#             raise NotImplementedError("Can't create User and UserProfile without database save")

#         user = User.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password1'],is_staff=False)
    
#         user_profile = profile(user=user,age=self.cleaned_data['age'],profilepicture=self.cleaned_data['profilepicture']) 
#         user_profile.save()
#         return user, user_profile