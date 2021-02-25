from django.contrib import admin
from .models import Category, Blog


admin.site.site_header = "داشبورد توسعه دهندگان"



# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "public", "created")
    list_filter = ("status", "public", "created")
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)