from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from Backend.custom_auth.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', "date_of_birth", 'is_staff', 'is_active',)
    list_filter = ('email', "date_of_birth", 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', "date_of_birth")}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', "date_of_birth")}
        ),
    )
    search_fields = ('email', "date_of_birth",)
    ordering = ('email', "date_of_birth",)