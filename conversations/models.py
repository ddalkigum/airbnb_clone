from django.db import models
from core.models import TimeStampModel


class Conversation(TimeStampModel):

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )
