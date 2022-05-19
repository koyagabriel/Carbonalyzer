import json
from pathlib import Path
from faker import Faker
from django.utils import timezone
from api.models import *

fake = Faker()

# Data seeded here are for testing purposes only


def seed_usage_types():
    file_path = Path(__file__).resolve().parent / "data/usage_types.json"
    with open(file_path) as fp:
        data = json.load(fp)
        for value in data:
            if not UsageType.objects.filter(**value).exists():
                UsageType(**value).save()

    print("Successfully loaded usage types")


def seed_sample_users_with_usages():
    sample_password = "sample_password"  # password was created for testing purposes.
    usage_types = UsageType.objects.all()
    try:
        master_sample_user = User(email="carbon@dioxide.com", first_name="Carbon", last_name="Dioxide")
        master_sample_user.set_password(sample_password)
        master_sample_user.save()
        seed_sample_usages(master_sample_user, usage_types)
        print("Created user email: {0}, password: {1}".format("carbon@dioxide.com", sample_password))
    except Exception:
        pass

    for _ in range(20):
        user_data = {
            "email": fake.unique.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": fake.street_suffix()
        }
        try:
            user = User(**user_data)
            user.set_password(sample_password)
            user.save()
            seed_sample_usages(user, usage_types)
            print("Created user email: {0}, password: {1}".format(user_data['email'], sample_password))
        except Exception:
            pass

    print("Successfully loaded sample users with their usage records")


def seed_sample_usages(user, list_usage_types):

    for usage_typ in list_usage_types:
        for _ in range(200):
            Usage(user=user,
                  usage_type=usage_typ,
                  amount=fake.pyfloat(left_digits=2, right_digits=3, positive=True),
                  usage_at=fake.date_time(tzinfo=timezone.utc)
                  ).save()


def main():
    seed_usage_types()
    seed_sample_users_with_usages()
