from django.apps import AppConfig


class RbacApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RBAC_API'

    # def ready(self):
    #     from .models import Role
    #     Role.create_default_roles()