from django.contrib import admin
from .models import User,Song,Singer,UserPermission,Role
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'role', 'is_active','is_staff', 'is_superuser',)
    search_fields = ('email', 'username')
    fieldsets = (
        (None, {'fields': ('email', 'password','username', 'role','is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups','last_login')}),
        # ('Personal info', {'fields': ('username', 'role')}),
        # ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        # ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role')}
        ),
    )
    filter_horizontal = ('user_permissions', 'groups')

admin.site.register(User, UserAdmin)

admin.site.register(Role)

class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('user',)
admin.site.register(UserPermission, UserPermissionAdmin)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','codename']
    search_fields = ['id']
    list_filter = ['id']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'singer','duration']
    search_fields = ['id', 'title']
    list_filter = ['id','title']

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']
    search_fields = ['id', 'name']
    list_filter = ['id']