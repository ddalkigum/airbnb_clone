from django.db import models
from core.models import TimeStampModel


class Reservation(TimeStampModel):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("finished", "Finished"),
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="pending")
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"
