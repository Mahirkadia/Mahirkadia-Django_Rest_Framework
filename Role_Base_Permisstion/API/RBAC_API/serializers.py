from rest_framework import serializers
from .models import User,Song,Singer,UserPermission,Role
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

class UserpermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = ('user','role', 'permission')
    def create(self, validated_data):
        user = validated_data.pop('user')
        permission = validated_data.pop('permission')
        role = validated_data.pop('role')
        user_permission = UserPermission.objects.create(user=user, permission=permission, role=role)
        return user_permission
    
class GroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True, required=False)
    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions', [])
        group = Group.objects.create(**validated_data)
        for permission in permissions_data:
            group.permissions.add(permission)
        return group

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=[])
    # permissions = PermissionSerializer(many=True, required=False)
    # permissions = serializers.JSONField(required=False, allow_null=True)
    permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True, required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'role', 'permissions')
        extra_kwargs = {'password': {'write_only': True}}

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        self.fields['role'].choices = User.get_role_choices()

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions', [])
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            role=validated_data['role']
        )
        # user.user_permissions.set(permissions_data)
        # return user
        for permission in permissions_data:
            UserPermission.objects.create(user=user, permission=permission)
        return user    
    def update(self, instance, validated_data):
        permissions = validated_data.pop('permissions', None)
        if permissions is not None:
            instance.user_permissions.set(permissions)
        return super().update(instance, validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)    

class SongSerializer(serializers.ModelSerializer):
    singer_name = serializers.SerializerMethodField()
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'singer_name', 'duration']  
        
    def get_singer_name(self, obj):
        return obj.singer.name
              
class SingerSerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender','songs']
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name', 'description' ,'permissions']
    def create(self, validated_data):
        role = Role.objects.create(**validated_data)
        return role


