from factory.django import DjangoModelFactory
from factory import Faker
from api.models import UsageType


class UsageTypeFactory(DjangoModelFactory):

    class Meta:
        model = UsageType

    name = Faker("pystr", min_chars=5, max_chars=15)
    unit = Faker("pystr", min_chars=1, max_chars=3)
    factor = Faker("pyfloat", positive=True, left_digits=2, right_digits=2)
