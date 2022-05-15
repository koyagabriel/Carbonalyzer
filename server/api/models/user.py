from django.contrib.auth.models import AbstractUser
from django.db.models import (EmailField, CharField)
from .base import BaseModel, BaseManager


class User(AbstractUser, BaseModel):
    email = EmailField(unique=True)
    username = CharField(max_length=150, unique=False, blank=True)
    first_name = CharField(max_length=150, blank=False)
    last_name = CharField(max_length=150, blank=False)

    objects = BaseManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "api_users"

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
