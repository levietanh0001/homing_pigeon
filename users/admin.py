from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

from .models import CustomUser


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email',)
    list_filter = ('email', 'is_active', 'is_staff', 'created_at', 'updated_at')
    ordering = ('-updated_at',)
    list_display = ('email', 'is_active', 'is_staff', 'created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    fieldsets = (
        # Other fieldsets

        ('Group Permissions', {
            'fields': ('groups', 'user_permissions', )
        }),
    )



admin.site.register(CustomUser, UserAdminConfig)