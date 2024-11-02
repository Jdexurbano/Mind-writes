from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    #specify the fields to display in the admin
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('avatar',)}),
    )

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)