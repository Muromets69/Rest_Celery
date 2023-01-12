from rest_framework import serializers
from .models import Car
from django.contrib.auth import get_user_model

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("__all__")
        
class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id',"username",'email','password')