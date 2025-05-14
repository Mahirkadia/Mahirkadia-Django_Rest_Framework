from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.authentication import SessionAuthentication
from .models import *
from .serializers import *
from .permission import *
from rest_framework.response import  Response
from rest_framework.views import APIView,status
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterViewSet(APIView):
    def post(self, request):
        serializer = RegiesterSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({
                'status': 403,
                'errors': serializer.errors,
                'msg': 'some error give'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Save the user and get the user instance directly
        user = serializer.save()
        
        # Generate tokens for the user
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'status': 200,
            'payload': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


class LoginViewSet(APIView):
    def post(self,request):
        email=request.data.get('email') 
        password=request.data.get('password') 
        if not email or not password:
            return Response({
                'status': 403,
                'msg': 'email & pass are required'
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            user=CustomeUser.objects.get(email=email)
        except CustomeUser.DoesNotExist:
            return Response({'status': 403,'msg': 'some error give' }, status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(password):
                return Response({'status': 403, 'msg': 'some error give' }, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        return Response({'status': 200,'user': {'email': user.email,'role': user.role,'firstname': user.firstname,'lastname': user.lastname},
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    
    
class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    permission_classes = [IsManagerOrReadOnly]
    authentication_classes=[SessionAuthentication]

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsManagerOrReadOnly]
    authentication_classes=[SessionAuthentication]