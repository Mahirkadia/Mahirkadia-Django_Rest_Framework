from rest_framework import serializers
from .models import CustomeUser, Role, UserPermission, Singer, Song
from django.contrib.auth import get_user_model


class RegiesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = ['email', 'password', 'firstname', 'lastname', 'role']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = CustomeUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            firstname=validated_data.get('firstname', ''),
            lastname=validated_data.get('lastname', ''),
            role=validated_data.get('role', 'normal')
        )
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
