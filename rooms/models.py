from django.db import models
from django_countries.fields import CountryField
from core.models import TimeStampModel


class AbstractItem(TimeStampModel):

    name = models.CharField(
        max_length=50,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    pass

    class Meta:
        verbose_name = "Room type"


class Amenity(AbstractItem):

    pass

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    pass


class Meta:
    verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    pass

    class Meta:
        verbose_name = "House Rule"


class Room(TimeStampModel):

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    room_type = models.ForeignKey(
        "RoomType", on_delete=models.SET_NULL, related_name="rooms", null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name
