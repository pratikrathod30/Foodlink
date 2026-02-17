from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'role', 'organization_name', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Organization Info', {'fields': ('organization_name', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'organization_name', 'role', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    readonly_fields = ('last_login',)


admin.site.register(User, UserAdmin)
