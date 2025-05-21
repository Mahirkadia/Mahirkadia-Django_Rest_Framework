from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status,generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from user_app.api.serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.views import APIView,status
from rest_framework_simplejwt.tokens import Token

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == "POST":
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'No token found for this user'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Use POST to logout'}, status=status.HTTP_200_OK)

class LoginViewSet(APIView):
    def post(self,request):
        username=request.data.get('username') 
        password=request.data.get('password') 
        if not username or not password:
            return Response({
                'status': 403,
                'msg': 'user & pass are required'
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'status': 403,'msg': 'Invalid credentials' }, status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(password):
                return Response({'status': 403, 'msg': 'Invalid credentials' }, status=status.HTTP_400_BAD_REQUEST)
        
        # Generate tokens
        refresh = RefreshToken.for_user(user)
        
        # Get all projects
        from project_app.models import Project
        from project_app.serializers import ProjectSerializer
        
        # Get projects where user is owner or member
        from project_app.models import ProjectMember
        owned_projects = Project.objects.filter(owner=user)
        member_projects = Project.objects.filter(projectmember__user=user)
        all_projects = (owned_projects | member_projects).distinct()
        
        projects_data = ProjectSerializer(all_projects, many=True).data
        
        return Response({
            'status': 200,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'username': user.username,
            'projects': projects_data
        }, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def registarion_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            response_data = serializer.data
            response_data['id'] = account.id
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Use POST to register'}, status=status.HTTP_200_OK)

class UserDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,*awgs, **kawgs):
        try :
            return self.retrieve(request,*awgs, **kawgs)
        except User.DoesNotExist:
            return Response({'error':'User Not Found'},status=status.HTTP_404_NOT_FOUND)
    def put(self,request, *awgs, **kawgs):
        self.partial = False
        try :
            return self.update(request,*awgs, **kawgs)
        except User.DoesNotExist:
            return Response({'error':'User Not Found'},status=status.HTTP_404_NOT_FOUND)
    def path(self, request, *awgs, **kawgs):
        self.partial = True
        try :
            return self.update(request, *awgs, **kawgs)
        except User.DoesNotExist:
            return Response({'error':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,*awgs,**kawgs):
        try:
            user = self.get_object()
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)