from djongo import models
from django import forms
# Create your models here.
dishtypes=[
('Appetizers & Snacks','Appetizers & Snacks'),
('Bread Recipes','Bread Recipes'),
('Cake Recipes','Cake Recipes'),
('Candy and Fudge','Candy and Fudge'),
('Casserole Recipes','Casserole Recipes'),
('Christmas Cookies','Christmas Cookies'),
('Cocktail Recipes','Cocktail Recipes'),
('Cookie Recipes','Cookie Recipes'),
('Mac and Cheese Recipes','Mac and Cheese Recipes'),
('Main Dish','Main Dish'),
('Pasta Salad Recipes','Pasta Salad Recipes'),
('Pasta Recipes','Pasta Recipes'),
('Pie Recipes','Pie Recipes'),
('Pizza','Pizza'),
('Sandwiches','Sandwiches'),
('Sauces and Condiments','Sauces and Condiments'),
('Smoothie Recipes','Smoothie Recipes'),
('Soups, Stews, and Chili','Soups, Stews, and Chili'),
('Side Dish','Side Dish'),
('Salad','Salad')
]
cuisines=[
    ('Chinese','Chinese'),
    ('Indian','Indian'),
    ('Italian','Italian'),
    ('Mexican','Mexican'),
    ('Southern','Southern'),
    ('Thai','Thai')
]
categories=[
('condiments','condiments'),
('Legumes','Legumes'),
('Seasonings','Seasonings'),
('Alcohol','Alcohol'),
('Added Sweetners','Added Sweetners'),
('Dairy Alternatives','Dairy Alternatives'),
('Oils','Oils'),
('Nuts','Nuts'),
('Meats','Meats'),
('Vegetables','Vegetables'),
('Seafood','Seafood'),
('Fruits','Fruits'),
('Dairy','Dairy'),
('Fish','Fish'),
('Desserts&Snacks','Desserts&Snacks'),
('Soup','Soup'),
('Baking & Grains','Baking & Grains'),
('Spices','Spices'),
('Sauces','Sauces'),
('Beverages','Beverages'),
]
marks=[
      ('green','green'),('red','red'),('yellow','yellow')
]
class ingredient(models.Model):
    _id=models.ObjectIdField()
    name=models.CharField(max_length=25)
    category=models.CharField(max_length=25,choices=categories)
    image=models.TextField()

    def __str__(self):
        return self.name

class image(models.Model):
    url=models.TextField()

    class Meta:
        abstract=True

class ingredientused(models.Model):
    quantity=models.CharField(max_length=30)
    ingredient=models.CharField(max_length=40)
    directions=models.CharField(max_length=50,default=None,null=True,blank=True)
    class Meta:
        abstract=True

class time(models.Model):
    hh=models.IntegerField()
    mm=models.IntegerField()
    class Meta:
        abstract=True

class recipe(models.Model):
    _id=models.ObjectIdField()
    title=models.CharField(max_length=60)
    description=models.TextField()
    image=models.ArrayField(model_container=image)
    timetocook=models.EmbeddedField(model_container=time)
    instructions=models.TextField()
    cuisine=models.CharField(max_length=25,choices=cuisines,default='',null=True,blank=True)
    dishtype=models.CharField(max_length=35,choices=dishtypes,default='',null=True,blank=True)
    mark=models.CharField(max_length=7,choices=marks)
    ingredientdetails=models.ArrayField(model_container=ingredientused)
    
    def __str__(self):
        return self.title

