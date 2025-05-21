from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model=User
        fields=['username','email','password','password2','first_name','last_name']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error':'passwords must match'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'email already exists'})
        
        account = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']
        )
        account.set_password(password)
        account.save() 
        return account
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','first_name','last_name','date_joined']
        