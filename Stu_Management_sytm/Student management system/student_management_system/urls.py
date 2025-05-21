from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from student_management_system import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_management_app.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Add static files configuration
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
# Keep media files configuration
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
