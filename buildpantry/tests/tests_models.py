from buildpantry.models import ingredient, recipe, ingredientUsed
from django.test import TestCase

class TestModels(TestCase):
	

	def setUp(self):
		self.ingredient1 = ingredient.objects.create(
				name= 'Tomato',
				category= 'Vegetable',
				image= 'https://images.media-allrecipes.com/userphotos/125x70/4538031.jpg'
			)
		

		self.recipe1 = recipe.objects.create(
				title= "Beefy Chinese Dumplings",
				description= "I couldn't find a good lo mein recipe on here, so I'm posting mine.",
				#ingredients: self.ingredientUsed1
				cuisine = "Chinese",
				dishtype = "cc",
				mealtype = "main course",
				mark = "aa",
				instructions = " Prep15 m\n  \n  \n   Cook25 m\n   \n    \n      Ready In40 m\n            \n    \n\n\n     \n    \n     Bring a large pot of lightly salted water to a boil. Cook spaghetti in the boiling water until cooked through but firm to the bite, about 12 minutes; drain and transfer to a large bowl." ,
				images =    [
					            "https://images.media-allrecipes.com/userphotos/250x250/194673.jpg",
					            "https://images.media-allrecipes.com/userphotos/125x70/194673.jpg"
					        ],
				timetocook = "35 m"
			)
		self.ingredientUsed1=ingredientUsed.objects.create(
				recipe_name = self.recipe1,
				ingredient_name = self.ingredient1,
				quantity = "250 gm",
				directions = "finely chopped"
			)

	def test_ingredient_image(self):
		image= self.ingredient1.ingredient_image() if self.ingredient1.ingredient_image().find('img') else "https://images.media-allrecipes.com/userphotos/125x70/4538031.jpg"
		
		self.assertEquals(self.ingredient1.ingredient_image(),image) 

	def test_ingredient_name(self):
		
		self.assertEquals(self.ingredient1.__str__(),'Tomato')

	def test_recipe_title(self):
		self.assertEquals(self.recipe1.__str__(),"Beefy Chinese Dumplings")

