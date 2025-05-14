from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group,Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        if role:
            group, created = Group.objects.get_or_create(name=role.name.capitalize())
            user.groups.add(group)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = None
        super().save(*args, **kwargs)

    @staticmethod
    def get_role_choices():
        groups = Group.objects.all()
        return [(group.name.lower(), group.name) for group in groups]

@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created and instance.role and not instance.is_superuser:
        if isinstance(instance.role, str):
            role_name = instance.role
        else:
            role_name = instance.role.name
        group, _ = Group.objects.get_or_create(name=role_name.capitalize())
        instance.groups.add(group)

class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)
    permission = models.ManyToManyField(Permission, blank=True, related_name='user_permissions')

    def __str__(self):
        return f"{self.user.email} - {self.permission.name}"
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        all_permissions = Permission.objects.all()
        for permission in all_permissions:
            if not self.permission.filter(id=permission.id).exists():
                self.permission.add(permission)
        
class Singer(models.Model):
    Male = 1
    Female = 2
    Gender_Choices = (
        (Male, 'Male'),
        (Female, 'Female')
        )
    name = models.CharField(max_length=100 )
    gender = models.PositiveSmallIntegerField(choices=Gender_Choices, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Song(models.Model):
    title= models.CharField (max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')
    duration= models.IntegerField()

    def __str__(self):
        return self.title
    
class Role(models.Model):
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    USER = 'USER'
    
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_system_role = models.BooleanField(default=False)
    permissions = models.ManyToManyField(Permission, blank=True, related_name='roles')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if self.name == self.ADMIN:
            self.is_system_role = True
        super().save(*args, **kwargs)
    
    @classmethod
    def create_default_roles(cls):
        if not cls.objects.filter(name=cls.ADMIN).exists():
            super_admin = cls.objects.create(
                name=cls.ADMIN,
                description='System-wide administrator with all permissions',
                is_system_role=True
            )
            all_permissions = Permission.objects.all()
            super_admin.permissions.add(*all_permissions)

        if not cls.objects.filter(name=cls.MANAGER).exists():
            manager = cls.objects.create(
                name=cls.MANAGER,
                description='Manager with limited permissions',
                is_system_role=False
            )
            manager_permissions = [
                'add_song',
                'change_song',
                'delete_song',
                'view_song',
                'add_singer',
                'change_singer',
                'delete_singer',
                'view_singer'
            ]
            for permission_codename in manager_permissions:
                permission = Permission.objects.get(codename=permission_codename)
                manager.permissions.add(permission)
        if not cls.objects.filter(name=cls.USER).exists():
            user = cls.objects.create(
                name=cls.USER,
                description='Regular user with basic permissions',
                is_system_role=False
            )
            user_permissions = [
                'view_song',
                'view_singer'
            ]
            for permission_codename in user_permissions:
                permission = Permission.objects.get(codename=permission_codename)
                user.permissions.add(permission)