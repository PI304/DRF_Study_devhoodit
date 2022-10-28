from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.hashers import make_password

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'