from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from django.utils import timezone
from api.models import Usage
from .usage_type import UsageTypeFactory
from .user import UserFactory


class UsageFactory(DjangoModelFactory):

    class Meta:
        model = Usage

    user = SubFactory(UserFactory)
    usage_type = SubFactory(UsageTypeFactory)
    usage_at = Faker("date_time", tzinfo=timezone.utc)
    amount = Faker("pyfloat", left_digits=2, right_digits=3, positive=True)
