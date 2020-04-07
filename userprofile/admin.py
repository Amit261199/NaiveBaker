from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from userprofile.models import profile


class profileInline(admin.StackedInline):
    model = profile
    readonly_fields=('age','profilepicture','preview_image','favourites','searchhistory')
    can_delete = False
    verbose_name_plural = 'profile details'
    verbose_name= 'profile'
    def preview_image(self, obj):
        return obj.image()
    preview_image.allow_tags = True
    preview_image.short_description = 'Image display'
    

class UserAdmin(BaseUserAdmin):
    inlines=(profileInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
# Register your models here.
