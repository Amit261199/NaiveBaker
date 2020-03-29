from django.contrib import admin
from .models import ingredient,recipe,ingredientList

# Register your models here.
admin.site.site_header='Naive Baker admin'
admin.site.site_title='Naive Baker admin'
admin.site.index_title = 'Naive Baker administration'
admin.site.register(ingredient)
admin.site.register(recipe)





