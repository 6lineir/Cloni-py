from rest_framework import serializers
from blog.models import Blog, Category
from accounts.models import User



class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'email')









# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = ('__all__')

class addSerial(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('__all__')


# Blog Serlializers Api 

class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = ('__all__')


from accounts.models import User
class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('__all__')