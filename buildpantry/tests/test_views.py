from django.test import TestCase
from django.urls import reverse
from buildpantry.models import *
from django.contrib.auth import get_user_model

class TestViews(TestCase):

	
	def setUp(self):
		
		User=get_user_model()
		User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
		self.client.login(username='temporary',password='temporary')
	
	def test_recipe_all_GET(self):

		response=self.client.get(reverse('recipes_all'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'recipelist.html')

	def test_build_pantry_GET(self):
		
		response=self.client.get(reverse('buildpantry'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'buildpantry.html')





