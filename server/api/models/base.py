from django.db.models import (
    Model, DateTimeField, BooleanField, Manager
)
from django.utils import timezone


class BaseManager(Manager):

    def not_deleted(self):
        return self.get_queryset().filter(deleted=False)

    def deleted(self):
        return self.get_queryset().filter(deleted=True)


class BaseModel(Model):
    created_at = DateTimeField(default=timezone.now)
    updated_at = DateTimeField(default=timezone.now)
    deleted = BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
