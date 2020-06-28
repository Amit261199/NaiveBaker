from django.test import TestCase , Client
from userprofile.views import removeFromSearch, viewhistory , viewfavlist , home , userprofilepage , contactpage , logoutfromsite, signup_view , login_view
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime

class TestViews(TestCase):
    
    def test_home(self):
        client=Client()
        response=client.get(reverse(home))
        #print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')

    def test_removeFromSearch(self):      
        client=Client()
        user=get_user_model()
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
        client=Client()
        user=get_user_model()
        self.client.login(username='rasik', password='Naive@123')
        response = self.client.post(reverse(login_view))
        self.assertEquals(response.status_code,302)
    '''
    def test_signup(self):
        client=Client()
        response = self.client.post('/signup/',{
            'username':'john',
            'password':'corona',
            'dob': '1997-03-02'
        })
        self.assertEquals(response.status_code,302)
    '''