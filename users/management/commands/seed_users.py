from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "create seed-user"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=1)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "is_superuser": False,
                "is_staff": False,
                "avatar": None,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} User Created!"))
