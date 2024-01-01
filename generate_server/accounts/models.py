import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager

class CustomUserManager(UserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
           raise ValueError("邮箱地址无效")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        # user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self,email=None,password=None,**extra_fields):
       extra_fields.setdefault('is_staff',False)
       extra_fields.setdefault('is_superuser',False)
       extra_fields.setdefault('is_active',True)
       return self._create_user(email,password,**extra_fields)
  
    def create_superuser(self,email=None,password=None,**extra_fields):
       extra_fields.setdefault('is_staff',True)
       extra_fields.setdefault('is_superuser',True)
       extra_fields.setdefault('is_active',True)
       return self._create_user(email,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=100,blank=True,default='unknown')
    avatar = models.ImageField(upload_to='user_avatars',blank=True,null=True)
    
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

    def save(self,*args,**kwargs):
        super().set_password(self.password)
        return super().save(*args,**kwargs)