from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('singerapi', views.SingerViewSet, basename="singer")
router.register('songapi', views.SongViewSet, basename="song")
# router.register('register', views.RegisterViewSet, basename="register")
# router.register('login', views.LoginViewSet, basename="login")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),  # DRF login/logout views
    path('api/', include(router.urls)),
    path('register/',views.RegisterViewSet.as_view()),
    path('login/', views.LoginViewSet.as_view()),
    # path("singerapi/",views.SingerViewSet.as_view()),
    # path("songapi/",views.SingerViewSet.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]