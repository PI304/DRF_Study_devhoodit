from turtle import Turtle
from django.db import models
import uuid

class UserPrivate(models.Model):
    # primary key id is default
    login_id = models.CharField(max_length=40)
    password = models.CharField(max_length=200)
    uuid = models.UUIDField(default=uuid.uuid4)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"user login id: {self.login_id} uuid: {self.uuid}"
    

class User(models.Model):
    # primary key id is default
    nickname = models.CharField(max_length=40)
    uuid = models.ForeignKey(UserPrivate, on_delete=models.CASCADE)
    profile_img_url = models.CharField(max_length=400)
    profile_message = models.CharField(max_length=400)
    last_login = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"nickname: {self.nickname} uuid: {self.uuid}"