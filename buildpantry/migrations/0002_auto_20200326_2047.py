# Generated by Django 2.2.11 on 2020-03-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildpantry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(choices=[('None', None), ('Chinese', 'Chinese'), ('Indian', 'Indian'), ('Italian', 'Italian'), ('Mexican', 'Mexican'), ('Southern', 'Southern'), ('Thai', 'Thai')], default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dishtype',
            field=models.CharField(choices=[('None', None), ('Appetizers & Snacks', 'Appetizers & Snacks'), ('Bread Recipes', 'Bread Recipes'), ('Cake Recipes', 'Cake Recipes'), ('Candy and Fudge', 'Candy and Fudge'), ('Casserole Recipes', 'Casserole Recipes'), ('Christmas Cookies', 'Christmas Cookies'), ('Cocktail Recipes', 'Cocktail Recipes'), ('Cookie Recipes', 'Cookie Recipes'), ('Mac and Cheese Recipes', 'Mac and Cheese Recipes'), ('Main Dish', 'Main Dish'), ('Pasta Salad Recipes', 'Pasta Salad Recipes'), ('Pasta Recipes', 'Pasta Recipes'), ('Pie Recipes', 'Pie Recipes'), ('Pizza', 'Pizza'), ('Sandwiches', 'Sandwiches'), ('Sauces and Condiments', 'Sauces and Condiments'), ('Smoothie Recipes', 'Smoothie Recipes'), ('Soups, Stews, and Chili', 'Soups, Stews, and Chili'), ('Side Dish', 'Side Dish'), ('Salad', 'Salad')], default=None, max_length=35),
        ),
    ]
