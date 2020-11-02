from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    def handle(self, *args, **option):
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop-friendly workspace",
            "TV",
            "Crib",
            "High chair",
            "Self check-in",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
            "Piano",
            "Beachfront",
            "Waterfront",
            "Ski-in/Ski-out",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created"))