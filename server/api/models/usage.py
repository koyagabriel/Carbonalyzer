from django.db.models import (DateTimeField, FloatField, ForeignKey, PROTECT, CASCADE)
from api.models.base import BaseModel
from api.models.usage_type import UsageType
from api.models.user import User


class Usage(BaseModel):
    user = ForeignKey(User, on_delete=CASCADE, related_name='usages')
    usage_type = ForeignKey(UsageType, on_delete=PROTECT, related_name='usages')
    usage_at = DateTimeField()
    amount = FloatField()

    class Meta:
        db_table = "api_usages"
