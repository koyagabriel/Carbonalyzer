from django.db.models import (Model, DateTimeField, BooleanField)
from django.utils import timezone


class BaseModel(Model):
    created_at = DateTimeField(default=timezone.now)
    updated_at = DateTimeField(default=timezone.now)
    deleted = BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    @classmethod
    def not_deleted(cls):
        return cls.objects.all().filter(deleted=False)
