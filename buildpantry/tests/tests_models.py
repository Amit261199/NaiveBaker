from buildpantry.models import ingredient, recipe, ingredientUsed
from django.test import SimpleTestCase

class TestModels(TestCase):
	print("In class")

	def setUp(self):
		self.ingredient1 = ingredient.objects.create(
				name= 'Tomato',
				category= 'Vegetable',
				image= 'https://images.media-allrecipes.com/userphotos/125x70/4538031.jpg'
			)
		print("IN setup")

		self.recipe1 = recipe.objects.create(
				title= "Beefy Chinese Dumplings",
				description= "I couldn't find a good lo mein recipe on here, so I'm posting mine.",
				#ingredients: self.ingredientUsed1
				cuisine = "Chinese",
				dishtype = "cc",
				mealtype = "main course",
				mark = "aa",
				instruction = " Prep15 m\n  \n  \n   Cook25 m\n   \n    \n      Ready In40 m\n            \n    \n\n\n     \n    \n     Bring a large pot of lightly salted water to a boil. Cook spaghetti in the boiling water until cooked through but firm to the bite, about 12 minutes; drain and transfer to a large bowl." ,
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

	def ingredient_test_image(self):
		image= self.ingredient1.ingredient_image() if self.ingredient1.ingredient_image().find('img') else "https://images.media-allrecipes.com/userphotos/125x70/4538031.jpg"
		print("In test 1")
		self.assertEquals(self.ingredient1.ingredient_image(),image) 

	def ingredient_test_name(self):
		print("In test 2")
		self.assertEquals(self.ingredient1.__str__(),'Tomato')

	def recipe_test_title(self):
		self.assertEquals(self.recipe1.__str__(),"Beefy Chinese Dumplings")

	# def recipe_test_images(self):
	# 	self.assertEquals(self.recipe1.__)
print("in models")
