from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
UserAdmin.fieldsets[2][1]['fields'] = (
										'phone',
										'codeMelli', 
										'is_active', 
										'is_staff', 
										'is_author', 
										'groups', 
										'user_permissions'
									)
UserAdmin.list_display += ('is_author', 'phone', 'codeMelli','reffrall')

admin.site.register(User, UserAdmin)