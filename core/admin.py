from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Ocena

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Role", {"fields": ("is_lecturer", "is_student")}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Ocena)