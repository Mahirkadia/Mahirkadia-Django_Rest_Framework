from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return request.method in SAFE_METHODS        
        if request.user.is_superuser:
            return True
        if request.user.role == 'admin':
            return True
        for perm in request.user.user_permissions.all():
            if request.user.has_perm(f'{perm.content_type.app_label}.{perm.codename}'):
                return True
        return request.method in SAFE_METHODS

class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return request.method in SAFE_METHODS
        if request.user.is_superuser:
            return True
        if request.user.role == 'manager' and request.method in ['PUT', 'PATCH']:
            return True
        for perm in request.user.user_permissions.all():
            if request.user.has_perm(f'{perm.content_type.app_label}.{perm.codename}'):
                return True
        return request.method in SAFE_METHODS

class IsExtraReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return request.method in SAFE_METHODS
        if request.user.is_superuser:
            return True
        if request.user.role == 'extra' and request.method in SAFE_METHODS:
            return True
        for perm in request.user.user_permissions.all():
            if request.user.has_perm(f'{perm.content_type.app_label}.{perm.codename}'):
                return True
        return request.method in SAFE_METHODS







# class IsAdminOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return request.method in SAFE_METHODS
#         if request.user.is_authenticated:
#             if request.user.is_superuser:
#                 return True
#             if request.user.role == 'admin':
#                 return True
#             if request.method in SAFE_METHODS:
#                 return True
#             for perm in request.user.user_permissions.all():
#                 if request.user.has_perm(f'{perm.content_type.app_label}.{perm.codename}'):
#                     if request.method in ['PUT', 'PATCH', 'DELETE', 'POST', 'GET', 'HEAD', 'OPTIONS']:
#                         return True
#         return False

# class IsManagerOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return request.method in SAFE_METHODS
#         if request.user.is_authenticated:
#             if request.user.is_superuser:
#                 return True
#             if request.user.role == 'manager' and request.method in ['PUT', 'PATCH']:
#                 return True
#             if request.method in SAFE_METHODS:
#                 return True
#             for perm in request.user.user_permissions.all():
#                 if request.user.has_perm(f'{perm.content_type.app_label}.{perm.codename}'):
#                     if request.method in ['PUT', 'PATCH', 'DELETE', 'POST', 'GET', 'HEAD', 'OPTIONS']:
#                         return True
#         return False

# class IsExtraReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return request.method in SAFE_METHODS
#         # if request.user.user_permissions:
#         #     return True
#         if request.user.is_authenticated:
#             if request.user.is_superuser:
#                 return True
#             if request.user.role == 'extra' and request.method in SAFE_METHODS:
#                 return True
#             # if request.user.user_permissions.exists():
#                 # Iterate over all permissions and check if any allow the current request method
#             for perm in request.user.user_permissions.all():
#                 if request.user.has_perm(f'{perm.content_type.app_label}.{perm.codename}'):
#                     if request.method in ['PUT', 'PATCH', 'DELETE', 'POST', 'GET', 'HEAD', 'OPTIONS']:
#                         return True
#         return request.method in SAFE_METHODS

