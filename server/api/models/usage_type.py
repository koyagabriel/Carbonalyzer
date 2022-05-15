from django.db.models.fields import (CharField, FloatField)
from .base import (BaseModel, BaseManager)


class UsageType(BaseModel):
    name = CharField(max_length=15)
    unit = CharField(max_length=10)
    factor = FloatField()

    objects = BaseManager()

    class Meta:
        unique_together = ['name', 'unit', 'factor']
        db_table = 'api_usage_types'
