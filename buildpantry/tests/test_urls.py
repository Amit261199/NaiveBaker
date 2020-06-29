from django.test import SimpleTestCase
from django.urls import reverse,resolve
from buildpantry.views import *

class TestUrls(SimpleTestCase):

	def test_buildpantry_url_is_resolved(self):
		url=reverse('buildpantry')
		print(resolve(url))
		self.assertEquals(resolve(url).func,buildpantry)


	def test_getRecipe_url_is_resolved(self):
		url=reverse('getRecipe')
		print(resolve(url))
		self.assertEquals(resolve(url).func,getRecipe)


	def test_displayRecipe_url_is_resolved(self):
		url=reverse('displayRecipe',args=['some-recipe'])
		print(resolve(url))
		self.assertEquals(resolve(url).func,displayRecipe)


	def test_recipes_all_url_is_resolved(self):
		url=reverse('recipes_all')
		print(resolve(url))
		self.assertEquals(resolve(url).func,recipes_all)


	def test_favourite_url_is_resolved(self):
		url=reverse('favourite')
		print(resolve(url))
		self.assertEquals(resolve(url).func,favourite)

	

