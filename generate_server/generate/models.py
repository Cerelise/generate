import uuid
from datetime import datetime

from django.db import models

from accounts.models import User

class Original(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    name = models.CharField(max_length=255)
    origin_pic = models.ImageField(upload_to='original')
    created_by = models.ForeignKey(User,related_name='origin',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_modify = models.BooleanField(default=False)

    def __str__(self) -> str:
         return self.name


class Result(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    modified_pic = models.ImageField(upload_to='result')
    created_by = models.ForeignKey(User,related_name='result',on_delete=models.CASCADE)
    origin = models.OneToOneField(Original,related_name='modified_time',on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True,blank=True)

    def save(self,*args,**kwargs):
        self.created_at = datetime.now()
        self.origin.created_at = self.created_at
        self.origin.save()
        super().save(*args,**kwargs)

