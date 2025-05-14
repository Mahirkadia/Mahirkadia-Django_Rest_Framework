from django.contrib import admin
from .models import CustomeUser,Role,UserPermission,Singer,Song

class CustomeUserAdmin(admin.ModelAdmin):
    list_display = ['id','email','role']

admin.site.register(CustomeUser,CustomeUserAdmin)

# admin.site.register(CustomeUser)
# admin.site.register(Role)
# admin.site.register(UserPermission)
# admin.site.register(Singer)
# admin.site.register(Song)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']

class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ['id','user']

class SingerAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','email','date_of_birth','address']

class SongAdmin(admin.ModelAdmin):
    list_display = ['id','title','singer']

admin.site.register(Role, RoleAdmin)
admin.site.register(UserPermission, UserPermissionAdmin)
admin.site.register(Singer, SingerAdmin)
admin.site.register(Song, SongAdmin)