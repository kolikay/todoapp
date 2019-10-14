from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Handles management of user profiles"""
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('Email must be provided')
        if not name:
            raise ValueError('Name must be provided')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

class UserTodoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    todo = models.CharField(max_length=100)
    guide_lines = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.todo