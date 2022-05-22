from factory.django import DjangoModelFactory
from faker import Faker
from factory import Faker as FactoryFaker
from api.models import User
from api.serializers.user import UserSerializer


class UserFactory(DjangoModelFactory):

    class Meta:
        model = User

    email = FactoryFaker("email")
    password = FactoryFaker("pystr", max_chars=15, min_chars=8)
    last_name = FactoryFaker("last_name")
    first_name = FactoryFaker("first_name")
    username = FactoryFaker("street_suffix")

    @classmethod
    def get_raw_data(cls, instance=None, set_password=True):
        if not isinstance(instance, User):
            instance = cls.build()
        raw_data = UserSerializer(instance).data

        if set_password:
            raw_data |= {'password': Faker().pystr(min_chars=8, max_chars=15)}

        return raw_data



