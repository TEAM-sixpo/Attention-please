from django.contrib import admin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'nickname', 'email', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    
    
admin.site.register(CustomUser, CustomUserAdmin)
