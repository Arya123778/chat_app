from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display=['email','username','is_online','is_staff']
    list_filter=['is_online','is_staff']
    fieldsets = UserAdmin.fieldsets+(
        ('Extra Info',{'fields':('bio','avatar','is_online')}),
    )