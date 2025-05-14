from rest_framework import generics, status,permissions
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import status,mixins,generics,viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import Group
from .models import User,Song,Singer,UserPermission,Role
from .serializers import UserSerializer,SingerSerializer,SongSerializer,GroupSerializer,LoginSerializer,UserpermissionSerializer,RoleSerializer
from .permissions import IsAdminOrReadOnly,IsManagerOrReadOnly,IsExtraReadOnly

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # if not request.user.is_superuser:
        #     return Response({"detail": "Only superusers can register new users with specific permissions."}, status=403)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)      
    
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'User logged in successfully',
            })
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsManagerOrReadOnly]
 
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAdminOrReadOnly]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsManagerOrReadOnly]
        elif self.action in ['destroy']:
            permission_classes = [IsAdminOrReadOnly]
        elif self.action in ['retrieve', 'list']:
            permission_classes = [IsAdminOrReadOnly, IsManagerOrReadOnly, IsExtraReadOnly]
        else:
            permission_classes = [IsAdminOrReadOnly, IsManagerOrReadOnly, IsExtraReadOnly]
        return [permission() for permission in permission_classes]  
    
class SingerViewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
class GroupCreateView(generics.CreateAPIView):
    serializer_class = GroupSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser] 

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied(detail="Only superusers can create groups.")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group_name = serializer.validated_data['name']
        permissions = serializer.validated_data.get('permissions', [])

        group, created = Group.objects.get_or_create(name=group_name, defaults={'permissions': permissions})
        if created:
            return Response({'detail': f'Group "{group_name}" created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': f'Group "{group_name}" already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
class UserPermissionView(generics.CreateAPIView ):
    queryset = UserPermission.objects.all()
    serializer_class = UserpermissionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]


class RoleViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
