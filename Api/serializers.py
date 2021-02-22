from rest_framework import serializers



# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = ('__all__')



# Blog Serlializers Api 
from blog.models import Blog
class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = ('__all__')


from django.contrib.auth.models import User
class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('__all__')