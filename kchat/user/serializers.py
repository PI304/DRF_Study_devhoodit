from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):

    nickname = serializers.CharField(
        max_length=40
    )

    uuid = serializers.CharField(
        read_only=True
    )

    profile_img_url = serializers.CharField(
        max_length=400
    )

    profile_message = serializers.CharField(
        max_length=400
    )

    last_login = serializers.DateTimeField(

    )

    class Meta:
        pass


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    
    user = UserSerializer()

    login_id = serializers.CharField(
        max_length=40
    )
    
    password = serializers.CharField(
        max_langth=200,
        write_only=True,
        required=True,
        help_text='Password',
        style={'input_type': 'password'}
        )
    
    uuid = serializers.UUIDField(
        format='hex_varbose'
    )

    email = serializers.EmailField(

    )

    create_at = serializers.DateTimeField(

    )
    
    class Meta:
        model = User