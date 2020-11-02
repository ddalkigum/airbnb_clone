import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms.models import Room, RoomType, Amenity, Facility, HouseRule, Photo
from users.models import User


class Command(BaseCommand):
    help = "create rooms"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=1)

    def handle(self, *args, **options):
        hosts = User.objects.all()
        room_type = RoomType.objects.all()
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(hosts),
                "room_type": lambda x: random.choice(room_type),
                "guests": lambda x: random.randint(1, 5),
                "price": lambda x: random.randint(25000, 50000),
                "beds": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
            },
        )
        clean_room = seeder.execute()
        clean_room_pk = flatten(list(clean_room.values()))
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        rules = HouseRule.objects.all()
        for pk in clean_room_pk:
            room_pk = Room.objects.get(pk=pk)
            for i in range(3, random.randint(12, 30)):
                Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room_pk,
                    file=f"/room_photos/{random.randint(1, 15)}.jpeg",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_pk.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_pk.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_pk.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} Room Created!"))
