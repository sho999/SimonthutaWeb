from django.contrib import admin
from . models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    
    list_display = ('email', 'first_name', 'last_name', 'username', 'city', 'role')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
    
    
# Register your models here.
admin.site.register(User, UserAdmin)
    