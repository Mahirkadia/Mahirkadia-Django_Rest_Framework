from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager,AbstractBaseUser,PermissionsMixin

class CustomeManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email Must")
        email=self.normalize_email(email)
        user= self.model(email=email,**extra_fields)
        user.is_active=True
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        return self.create_user(email, password, **extra_fields)

class CustomeUser(AbstractUser):
    ROLE_CHOICES=(
        ("admin","Admin"),
        ("manager","Manager"),
        ("normal","Normal")
    )
    username= None
    email=models.EmailField("Email Field",unique=True)
    firstname = models.CharField(max_length=50,null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects= CustomeManager()
    def __str__(self):
        return self.email

class Role(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

class UserPermission(models.Model):
    user=models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    permission= models.CharField(max_length=50)

class Singer(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    date_of_birth=models.DateField()
    address=models.TextField()

    def __str__(self):
        return self.name

class Song(models.Model):
    title=models.CharField(max_length=50)
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
   
