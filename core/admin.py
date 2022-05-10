from django.contrib import admin
from core.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','first_name','last_name','is_staff','is_active')
    class Meta:
        model = CustomUser

    # fieldsets = (
    #     (None, {
    #         "fields": (
    #             'email','first_name','last_name'
    #         ),
    #     }),
    #     ('Permissions',{'fields':('is_staff','is_active')}),
    # )
    

# Register your models here.
admin.site.register(CustomUser,UserAdmin)
admin.site.register(Reset)