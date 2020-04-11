from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from userprofile.models import profile


class profileInline(admin.StackedInline):
    model = profile
    readonly_fields=('dateofbirth','profilepicture','preview_image','favourites','searchhistory')
    can_delete = False
    verbose_name_plural = 'profile details'
    verbose_name= 'profile'
    def preview_image(self, obj):
        return obj.image()
    preview_image.allow_tags = True
    preview_image.short_description = 'Image display'

    
class staffMemberAdmin(BaseUserAdmin):
    verbose_name='Staff Member'
    verbose_name_plural="Staff Members"
    def queryset(self, request):
        return (super(staffMemberAdmin, self).queryset(request)
                .filter(is_staff=True))



admin.site.unregister(User)
admin.site.register(User,staffMemberAdmin)

# Register your models here.
