import uuid

from accounts.models import User
from django.db import models


class Origin(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='origin')
    created_by = models.ForeignKey(User,related_name='origin',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_modify = models.BooleanField(default=False)

    def __str__(self) -> str:
         return self.id


class Result(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    modified_pic = models.ImageField(upload_to='result')
    created_by = models.ForeignKey(User,related_name='result',on_delete=models.CASCADE)
    origin = models.OneToOneField(Origin,related_name='origin',on_delete=models.CASCADE)
    favorited = models.ManyToManyField(User,related_name='favorites')
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # def save(self,*args,**kwargs):
    #     self.created_at = datetime.now()
    #     self.origin.modified_at = self.created_at
    #     self.origin.save()
    #     super().save(*args,**kwargs)
