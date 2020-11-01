from django.db import models
from core.models import TimeStampModel


class List(TimeStampModel):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="lists"
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        print(self)
        return self
