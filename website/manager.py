from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils import timezone
class UserManager(BaseUserManager):
    def create_user(self, email, username, password, alias=None):
        if not email:
            raise ValueError("ENTER AN EMAIL")
        if not username:
            raise ValueError("ENTER A NAME")
        if not password:
            raise ValueError("ENTER A PASSWORD")
        if not alias:
            alias = username
        
        user = self.model(
             email = self.normalize_email(email),
             username = username,
             alias = alias)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password, alias=None):
        user =self.create_user(email, username, password, alias)
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user