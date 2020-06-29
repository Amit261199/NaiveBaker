from django.test import TestCase , Client
from userprofile.views import removeFromSearch, viewhistory , viewfavlist , home , userprofilepage , contactpage , logoutfromsite, signup_view , login_view
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime

class TestViews(TestCase):
    
    
    def test_home(self):
        client=Client()
        response=client.get(reverse(home))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')

    def test_removeFromSearch(self):      
        client=Client()
        self.client.login(username='rasik', password='Naive@123')
        response = self.client.post(reverse(login_view))
        response=client.get(reverse(removeFromSearch))
        self.assertEquals(response.status_code,405)
    
    def test_viewhistory(self):
        client=Client()
        response=client.get(reverse(viewhistory))
        #print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'history.html')
    
    def test_viewfavlist(self):
        client=Client()
        user=get_user_model()
        self.client.login(username='rasik', password='Naive@123')
        response = self.client.post(reverse(login_view))
        response=client.get(reverse(viewfavlist))
        #print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'favlist.html')
    
    def test_userprofilepage(self):
        client=Client()
        user=get_user_model()
        self.client.login(username='rasik', password='Naive@123')
        response = self.client.post(reverse(login_view))
        response=client.get(reverse(userprofilepage))
        #print(response)
        self.assertEquals(response.status_code,302)
    
    def test_contactpage(self):
        client=Client()
        response=client.get(reverse(contactpage))
        #print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'contact.html')

    def test_logoutfromsite(self):
        client=Client()
        user=get_user_model()
        self.client.login(username='rasik', password='Naive@123')
        response = self.client.post(reverse(login_view))
        response=client.get(reverse(logoutfromsite))
        self.assertEquals(response.status_code,302)

    def test_signup_view(self):
        client=Client()
        response=client.get(reverse(signup_view))
        self.assertEquals(response.status_code,200)

    def test_login_view(self):
        client=Client()
        response=client.get(reverse(login_view))
        self.assertEquals(response.status_code,200)
    
    def test_login(self):
        # client=Client()
        # user=get_user_model()
        self.client.login(username='rasik', password='Naive@123')
        response = self.client.post(reverse(login_view))
        self.assertEquals(response.status_code,302)

    
    def test_login2(self):
        # client=Client()
        # user=get_user_model()
        self.client.login(username='rasik', password='Naive@1234')
        response = self.client.post(reverse(login_view))
        self.assertEquals(response.status_code,302)
        self.assertEquals(response.url,"../login")
    
    def test_signup(self):
        response =self.client.post('/signup/',{
            'uname':'john',
            'psw':'corona',
            'psw-repeat':'corona',
            'dob': '02/03/1997',
            'email':'test_email@gmail.com'
        })
        self.assertEquals(response.status_code,302)
        self.assertEquals(response.url,"../login")
    
    def test_signup2(self):
        response =self.client.post('/signup/',{
            'uname':'john',
            'psw':'corona',
            'psw-repeat':'corona',
            'dob': '02/03/2021',
            'email':'test_email@gmail.com'
        })
        self.assertEquals(response.status_code,302)
        self.assertEquals(response.url,"../signup")
    
    def test_signup3(self):
        response =self.client.post('/signup/',{
            'uname':'rasik',
            'psw':'Navie@123',
            'psw-repeat':'Navie@123',
            'dob': '02/03/1987',
            'email':'test_email@gmail.com'
        })
        self.assertEquals(response.status_code,302)
        self.assertEquals(response.url,"../login")