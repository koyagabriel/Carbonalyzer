from django.core.management.base import BaseCommand, CommandError
from api import seed


class Command(BaseCommand):
    help = 'Seeds data into database'

    def handle(self, *args, **options):
        try:
            seed.main()
        except Exception as err:
            raise CommandError(err.args[0])

        self.stdout.write(self.style.SUCCESS("Successfully loaded seed file"))