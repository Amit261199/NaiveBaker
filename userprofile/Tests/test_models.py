from django.test import TestCase
from userprofile.models import profile, history
from buildpantry.models import recipe, ingredient, ingredientUsed
from django.contrib.auth import get_user_model
import datetime
import os
from django.core.files import File
import urllib

class TestModels(TestCase):
	

    def setUp(self):
        User=get_user_model()
        user=User.objects.create_user('temporary','temporary@gmail.com','temporary')
        dob=datetime.date(year=1999,month=12,day=20)
        self.profile=profile.objects.create(user=user,dateofbirth=dob)
        
        link='https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U'
        

        result = urllib.request.urlretrieve(link)

        self.profile.profilepicture.save(
            os.path.basename(link),
            File(open(result[0], 'rb'))
            )
        test_recipe = recipe.objects.create(
				title= "Beefy Chinese Dumplings",
				description= "I couldn't find a good lo mein recipe on here, so I'm posting mine.",
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

        self.profile.favourites.add(test_recipe)
        self.hist=history.objects.create(userprofile=self.profile,recipe_searched=test_recipe,timestamp=datetime.datetime.utcnow())
        
    def test_profile_picture(self):
        self.assertTrue('<img src="' in self.profile.image().__str__())