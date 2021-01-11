from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude=("password","last_login",'user_permissions',"groups","is_superuser","is_staff","is_active","date_joined","favs")
    
