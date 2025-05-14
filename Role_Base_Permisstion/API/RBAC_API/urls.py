from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'song', SongViewset,basename='song')
router.register(r'singer', SingerViewset,basename='singer')
router.register(r'role', RoleViewset, basename='role')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    path('userpermission/', UserPermissionView.as_view(), name='userpermission'),
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),

]
