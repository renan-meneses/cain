from django.contrib.auth.models import AbstractBaseUser  # isort:skip
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, password, **other_fields):
        if not email:
            raise ValueError("Provide email")
        email = self.normalize_email(email)
        user = self.model(
            email=email, name=name, surname=surname, **other_fields
        )  # noaq: E501
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, surname, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("staff privilege must be assigned to superuser")
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "superuser privilege must be assigned to superuser"
            )  # noaq: E501

        return self.create_user(email, name, surname, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=False)
    surname = models.CharField(max_length=150, blank=False)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "surname"]

    def __str__(self):
        return self.name
