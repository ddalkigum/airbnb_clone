from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    def handle(self, *args, **option):
        facilities = [
            "free parking on premises",
            "Gym",
            "Hot tub,",
            "Pool",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("facilities created"))