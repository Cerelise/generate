import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
           raise ValueError("邮箱地址无效")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()

        return user
  
    def create_superuser(self,email=None,password=None,**extra_fields):
       extra_fields.setdefault('is_staff',True)
       extra_fields.setdefault('is_superuser',True)
       extra_fields.setdefault('is_active',True)

       if extra_fields.get("is_staff") is not True:
           return ValueError("超级用户的is_staff属性必须为True")

       if extra_fields.get("is_superuser") is not True:
           return ValueError("超级用户的is_superuser属性必须为True")

       return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,blank=True,default='unknown')
    avatar = models.ImageField(upload_to='user_avatars',blank=True,null=True)
    phone = models.CharField(max_length=30,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    
    upload_count = models.IntegerField(default=0)

    is_vip = models.BooleanField(default=False)
    vip_length = models.IntegerField(default=0)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True,null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     self.set_password(self.password)
    #     return super().save(update_fields=['password'])

    def __str__(self):
        return self.username