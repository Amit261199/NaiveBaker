from django.test import TestCase,Client
from django.urls import reverse
from buildpantry.models import *
from django.contrib.auth import get_user_model

class TestViews(TestCase):
	class MockUser:
		is_authenticated=True
	
	def test_recipe_all_GET(self):
		client=Client()
		User = get_user_model()
		user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
		self.client.login(username='temporary', password='temporary')
		response=client.get(reverse('recipes_all'))
		response.user=MockUser()
		print(response['location'])
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'buildpantry/recipelist.html')

	def test_build_pantry_GET(self):
		client=Client()
		User = get_user_model()
		user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
		self.client.login(username='temporary', password='temporary')
		response=client.get(reverse('buildpantry'))
		response.user=MockUser()
		print(response['location'])
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'buildpantry/buildpantry.html')





