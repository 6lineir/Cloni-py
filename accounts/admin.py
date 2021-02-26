from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
UserAdmin.fieldsets[1][1]['fields'] += (
										'phone',
										'codeMelli', 
										'is_author', 
									)
UserAdmin.list_display += ('is_author', 'phone', 'codeMelli','reffrall')

admin.site.register(User, UserAdmin)