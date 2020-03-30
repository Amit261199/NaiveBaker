from django.contrib import admin
from .models import ingredient,recipe,ingredientUsed




class ingredientList_inline(admin.TabularInline):
    model = ingredientUsed
    extra = 1
    verbose_name = "Ingredient Used"
    verbose_name_plural = "Ingredients Used"

class recipeAdmin(admin.ModelAdmin):
    inlines=[ingredientList_inline,]
    fields=('title','description','images','preview_image',('cuisine','dishtype'),('mealtype','mark'),'timetocook')
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return obj.recipe_image()
    preview_image.allow_tags = True
    preview_image.short_description = 'Image display'

class ingredientAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_image']
    def preview_image(self, obj):
        return obj.ingredient_image()
    preview_image.allow_tags = True
    preview_image.short_description = 'Image display'
# Register your models here.
admin.site.site_header='Naive Baker admin'
admin.site.site_title='Naive Baker admin'
admin.site.index_title = 'Naive Baker administration'
admin.site.register(ingredient,ingredientAdmin)
admin.site.register(recipe,recipeAdmin)






