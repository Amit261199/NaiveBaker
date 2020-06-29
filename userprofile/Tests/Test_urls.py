from django.test import SimpleTestCase
from django.urls import reverse, resolve
from userprofile.views import userprofilepage, viewfavlist, viewhistory , removeFromSearch
class TestUrls(SimpleTestCase):

    def test_url_is_userprofilepage(self):
        url = reverse('userprofilepage')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,userprofilepage)

    def test_url_is_viewfavlist(self):
        url = reverse('viewfavlist')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,viewfavlist)

    def test_url_is_viewhistory(self):
        url = reverse('viewhistory')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,viewhistory)
    
    def test_url_is_removeFromSearch(self):
        url = reverse('removeFromSearch')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,removeFromSearch)
    
        